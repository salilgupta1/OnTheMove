from django.shortcuts import render
from Activities.models import OnthemoveActivity as Act, OnthemoveLocation as Loc

# Create your views here.

def details(request, id):
	activity = Act.objects.get(activity_id=id)
	context = {}
	context["activity_name"] = activity.activity_name
	context["start_time"] = activity.start_time
	location = Loc.objects.get(location_id = activity.location_id)
	context["location_name"] = location.location_name
	context["date"] = activity.date #not work


	return render(request,"Activities/details.html", context)
