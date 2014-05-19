from django.shortcuts import render
from Activities.models import OnthemoveActivity as Act, OnthemoveLocation as Loc
from Users.models import OnthemoveUser as User
from django.core.mail import send_mail,EmailMultiAlternatives
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.urlresolvers import reverse
from forms import ActivityForm, LocationForm
from django.core.context_processors import csrf
from datetime import datetime
import urllib2, json

# Create your views here.
def accept_user(request):
	pass
@ensure_csrf_cookie
def details(request, id):
	activity = Act.objects.get(activity_id=id)
	if request.is_ajax():
		if request.user.is_authenticated():
			userName = request.user.first_name +" "+ request.user.last_name
			#userAge = request.user.age
			#userGen = request.user.gender
				#send_mail('Request to Join Activity on OnTheMove',"Hi "+activity.owner_id.user.first_name+", "+userName+" has requested to join your activity "+activity.activity_name+". Here is an overview of "+userName+" profile Age: 24, Gender: Male",
				#	'noreply@onthemove.com',['salil.gupta323@gmail.com',activity.owner_id.user.email],fail_silently=False)
				
			subject='Request to Join Activity on OnTheMove'
			from_email = 'noreply@onthemove.com'
			text_content = "Hi "+ activity.owner_id.user.first_name+", "+userName+" has requested to join your activity "+activity.activity_name+". Here is an overview of "+userName+" profile Age: 24, Gender: Male"
			html_content = "<div>Hi "+activity.owner_id.user.first_name+",</div><div><p>"+userName+" has requested to join your activity "+activity.activity_name+".</p> Here is an overview of "+userName+"'s profile</div><div> To add "+userName+" to your activity click the link below <p> <a href=''>Accept "+userName+"</a></p></div>"
			msg = EmailMultiAlternatives(subject, text_content, from_email, ['salil.gupta323@gmail.com'])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			return HttpResponse("Thanks!")
		#else:
		#	return HttpResponse(0)
	else:
		context = {}
		context["activity_name"] = activity.activity_name
		context["start_time"] = activity.start_time
		location = activity.location_id
		context["location_name"] = location.location_name
		context["date"] = activity.date.strftime('%m/%d/%Y') #not work
		context["address"] = location.address
		context["zipcode"] = location.zipcode
		context["state"] = location.state
		context["skill"] = activity.skill_level
		context["attendees"] = activity.attendees
		context["city"] = location.city
		context['path'] = request.path
		if activity.attendees.count()== activity.max_num_attendees:
			context['max_out']=True
		if activity.attendees.filter()
		return render(request,"Activities/details.html", context)

def create_Activity(request, location_id):
	if request.method == 'POST':
		form = ActivityForm(request.POST)

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

		request.GET = request.GET.copy()
		request.GET['date'] = dt
		request.GET['start_time'] = st 
		request.GET['end_time'] = et 
		request.GET['activity_name'] = name
		request.GET['max_num_attendees'] = max_num
		request.GET['min_num_attendees'] = min_num
		request.GET['skill_level'] = skill

		form1 = ActivityForm(request.GET)

		m = form1.save(commit=False)
		location = Loc.objects.get(location_id=location_id)
		owner = User.objects.get(id=1)  ### FIX LATER WHEN USERS ARE CREATED

		m.location_id = location
		m.owner_id = owner

		if form1.is_valid():
			x=form1.save()
			return HttpResponseRedirect(reverse("Activities:details",args=(x.pk,)))
	else:
		form = ActivityForm()
	context = {}
	context.update(csrf(request))
	context['create_form'] = form
	context['id'] = location_id
	return render(request,"Activities/createActivity.html",context)

def create_Location(request):
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			name = request.POST.get('location_name')
			street = request.POST.get('address')
			city = request.POST.get('city')
			state = request.POST.get('state')
			zipcode = request.POST.get('zipcode')
			rating = request.POST.get('location_rate')

			# gmaps = GoogleMaps("AIzaSyBP1fyEFwMdXYuajcnYFdt2QS--mDspV4o")
			addr_str = street + ", " + city + ", " + state
			# print gmaps
			# data = gmaps.address_to_latlng(addr_str)

			r = geocode(addr_str)
			lat = r['lat']
			lng = r['lng']

			m = form.save(commit=False)
			m.longitude = lng
			m.latitude = lat
			location_obj = form.save()
			location_id = location_obj.location_id
			lng = location_obj.longitude
			lat = location_obj.latitude
			return HttpResponseRedirect(reverse("Activities:create_Activity", args=(location_id,)))
	else:
		form = LocationForm()
	context = {}
	context.update(csrf(request))
	context['create_form'] = form
	return render(request,"Activities/createLocation.html",context)

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