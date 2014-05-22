from django.shortcuts import render
from Activities.models import OnthemoveActivity as Act, OnthemoveLocation as Loc
from Users.models import OnthemoveUser 
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.urlresolvers import reverse
from forms import ActivityForm, LocationForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from datetime import datetime
import urllib2, json
from django.template.loader import get_template
from django.template import Context
from Activities import yelp_api

# Create your views here.

@login_required
def addUser(request,activity_id,user_id):
	activity = Act.objects.get(activity_id=activity_id)
	user = OnthemoveUser.objects.get(pk = user_id)
	if request.method =='POST':
		print 'here'
		is_add = request.POST.get('add')
		is_ignore = request.POST.get('ignore')
		if is_add:
			activity.pending.remove(user)
			activity.attendees.add(user)
			context = {}
			context['added'] = user.user.first_name+" has been added to your activity"
		elif is_ignore:
			context['added'] = User.user.first_name+" will not be added to your activity"	
		return render(request,"Activities/addUserSuccess.html",context)
	else:
		context = {}
		context['user_name'] = user.user.first_name +" "+user.user.last_name
		context['user_age'] = user.age
		context['user_gender']= user.gender
		context['activity_name'] = activity.activity_name
		context['path']=request.path
		context.update(csrf(request))
		return render(request,"Activities/addUser.html",context)
@ensure_csrf_cookie
def details(request, id):
	activity = Act.objects.get(activity_id=id)
	if request.is_ajax():
		if request.user.is_authenticated():
			activity.pending.add(request.user.onthemoveuser)
			userName = request.user.first_name +" "+ request.user.last_name	

			subject='Request to Join Activity on OnTheMove'
			from_email = 'noreply@onthemove.com'
			
			text_content = ("Hi "+ activity.owner_id.user.first_name+", "+userName+" has requested " 
				"to join your activity "+activity.activity_name+".")

			html_content = get_template('Activities/enrollEmail.html').render(
				Context({
					"protocol":"http",
					"domain":request.get_host(),
					"userName":userName,
					"owner":activity.owner_id.user.first_name,
					"activity_name":activity.activity_name,
					"aid":id,
					"uid":request.user.onthemoveuser.pk
				})
			)
			msg = EmailMultiAlternatives(subject, text_content, from_email,[activity.owner_id.user.email,'salil.gupta323@gmail.com'])## change email
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			return HttpResponse("Thanks!")
	else:
		context = {}
		context["activity_name"] = activity.activity_name
		context["start_time"] = activity.start_time
		location = activity.location_id
		context["location_name"] = location.location_name
		context["date"] = activity.date.strftime('%m/%d/%Y') #not work
		context["address"] = location.address
		context["zipcode"] = location.zipcode
		context["rating"] = location.location_rate
		context["state"] = location.state
		context["skill"] = activity.skill_level
		context["attendees"] = activity.attendees
		context["city"] = location.city
		context['owner'] = activity.owner_id
		context['path'] = request.path
		context['img_url'] = location.location_img_url
		if request.user.is_authenticated():
			if activity.attendees.count()== activity.max_num_attendees:
				context['is_max_out']=True
			if activity.attendees.filter(pk = request.user.onthemoveuser.pk):
				context['is_enrolled']=True
			if activity.pending.filter(pk=request.user.onthemoveuser.pk):
				context['is_pending']=True
			if activity.owner_id.pk == request.user.onthemoveuser.pk:
				context['is_owner']=True
		return render(request,"Activities/details.html", context)

@login_required
def create_Activity(request):
	if request.method == 'POST':
		actForm = ActivityForm(request.POST)
		locForm = LocationForm(request.POST)

		# check for valid location
		if locForm.is_valid():
			street = request.POST.get('address')
			city = request.POST.get('city')
			state = request.POST.get('state')

			# get lat and long
			addr_str = street + ", " + city + ", " + state
			r = geocode(addr_str)
			lat = r['lat']
			lng = r['lng']

			m = locForm.save(commit=False)
			m.longitude = lng
			m.latitude = lat
			loc_name = m.location_name
			rating,img_url = yelp_api.get_yelp_data(loc_name,lng,lat)

			print img_url

			if rating == -1:
				m.location_rate = "no rating available"
			else:
				m.location_rate = rating

			
			if img_url == -1:
				m.location_img_url = "http://www.mountainmansocialmedia.com/_site/wp-content/themes/juiced/img/thumbnail-default.jpg"
			else:
				m.location_img_url = img_url
			
			location_obj = locForm.save()
			


			date = request.POST.get('date')
			start_time = request.POST.get('start_time')
			end_time = request.POST.get('end_time')
			name = request.POST.get('activity_name')
			max_num = request.POST.get('max_num_attendees')
			min_num = request.POST.get('min_num_attendees')
			skill = request.POST.get('skill_level')

			dt = datetime.strptime(date, "%m/%d/%Y")
			st = datetime.strptime(convert_Time(start_time), "%H:%M:%S")
			et = datetime.strptime(convert_Time(end_time), "%H:%M:%S")
			owner = request.user.onthemoveuser

			request.GET = request.GET.copy()
			request.GET['date'] = dt
			request.GET['start_time'] = st 
			request.GET['end_time'] = et 
			request.GET['activity_name'] = name
			request.GET['max_num_attendees'] = max_num
			request.GET['min_num_attendees'] = min_num
			request.GET['skill_level'] = skill
			request.GET['location_id'] = location_obj
			request.GET['owner_id'] = owner

			actForm1 = ActivityForm(request.GET)

			if actForm1.is_valid():
				x=actForm1.save(commit=False)
				x.location_id = location_obj
				x.owner_id = owner
				y = actForm1.save()
				print "here"
				return HttpResponseRedirect(reverse("Activities:details",args=(y.pk,)))
	else:
		actForm = ActivityForm()
		locForm = LocationForm()
	context = {}
	context.update(csrf(request))
	context['act_form'] = actForm
	context['loc_form'] = locForm

	return render(request,"Activities/createActivity.html", context)

def convert_Time(time):
	timeArray = time.split(":")
	hours = timeArray[0]
	timeArray2 = timeArray[1].split(" ")
	minutes = timeArray2[0]
	ampm = timeArray2[1]

	if (ampm == "PM" and int(hours) < 12):
		hours = int(hours) + 12
	if (ampm == "AM" and int(hours) == 12):
		hours = int(hours)
	return str(hours) + ":" + str(minutes) + ":" + str(0)

def geocode(addr):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" %   (urllib2.quote(addr.replace(' ', '+')))
    data = urllib2.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")
    return info