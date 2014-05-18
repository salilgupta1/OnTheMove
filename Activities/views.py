from django.shortcuts import render, render_to_response
from Activities.models import OnthemoveActivity as Act, OnthemoveLocation as Loc
from Users.models import OnthemoveUser as User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.urlresolvers import reverse
from forms import ActivityForm, LocationForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
import urllib2, json

# Create your views here.
@ensure_csrf_cookie
def details(request, id):
	activity = Act.objects.get(activity_id=id)
	if request.is_ajax():
		send_mail('Request to Join Activity on OnTheMove',"Hi "+activity.owner_id.user.first_name+",Jerry has requested to join your activity "+activity.activity_name+". Here is an overview of Jerry's profile Age: 24, Gender: Male",
			'noreply@onthemove.com',['salil.gupta323@gmail.com',activity.owner_id.user.email],fail_silently=False)
		return HttpResponse("The owner of the activity has been notified!")
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
		return render(request,"Activities/details.html", context)

@login_required
def create_Activity(request):
	if request.method == 'POST':
		actForm = ActivityForm(request.POST)
		locForm = LocationForm(request.POST)

		# check for valid location
		if locForm.is_valid():
			name = request.POST.get('location_name')
			street = request.POST.get('address')
			city = request.POST.get('city')
			state = request.POST.get('state')
			zipcode = request.POST.get('zipcode')
			rating = request.POST.get('location_rate')

			# get lat and long
			addr_str = street + ", " + city + ", " + state
			r = geocode(addr_str)
			lat = r['lat']
			lng = r['lng']

			m = locForm.save(commit=False)
			m.longitude = lng
			m.latitude = lat
			location_obj = locForm.save()
			location_id = location_obj.location_id

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

			location = Loc.objects.get(location_id=location_id)
			owner = User.objects.get(id=1)  ### FIX LATER WHEN USERS ARE CREATED
			#owner = request.user

			request.GET = request.GET.copy()
			request.GET['date'] = dt
			request.GET['start_time'] = st 
			request.GET['end_time'] = et 
			request.GET['activity_name'] = name
			request.GET['max_num_attendees'] = max_num
			request.GET['min_num_attendees'] = min_num
			request.GET['skill_level'] = skill
			request.GET['location_id'] = location
			request.GET['owner_id'] = owner

			actForm1 = ActivityForm(request.GET)

			if actForm1.is_valid():
				x=actForm1.save()
				return HttpResponseRedirect(reverse("Activities:details",args=(x.pk,)))
	else:
		actForm = ActivityForm()
		locForm = LocationForm()
	context = {}
	context.update(csrf(request))
	context['act_form'] = actForm
	context['loc_form'] = locForm

	return render_to_response("Activities/createActivity.html", context, RequestContext(request))

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