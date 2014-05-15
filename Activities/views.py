from django.shortcuts import render
from Activities.models import OnthemoveActivity as Act, OnthemoveLocation as Loc
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
#from django.core.urlresolvers import reverse

# Create your views here.
@ensure_csrf_cookie
def details(request, id):
	activity = Act.objects.get(activity_id=id)
	if request.is_ajax():
		send_mail('Request to Join Activity on OnTheMove',"Hi"+activity.owner_id.user.first_name+", Jerry has requested to \
			join your activity "+activity.activity_name+". Here is an overview of Jerry's profile",
			'noreply@onthemove.com',['salil.gupta323@gmail.com'],fail_silently=False)
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