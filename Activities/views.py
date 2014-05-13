from django.shortcuts import render
from Activities.models import OnthemoveActivity as Act, OnthemoveLocation as Loc
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def details(request, id):
	activity = Act.objects.get(activity_id=id)
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

	return render(request,"Activities/details.html", context)
def enroll(request):
	# pass
	# if request.method == 'POST':
	send_mail('Test OnTheMove','email sent successfully', 'No_reply@OnTheMove.com', ['ava.gu1990@gmail.com'], fail_silently = False)
		
	return HttpResponseRedirect(reverse("home"))
