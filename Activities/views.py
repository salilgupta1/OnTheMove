from django.shortcuts import render
# from Activites.model import OnthemoveActivity, OnthemoveLocation

# Create your views here.

def details(request, id):
	activity = OnthemoveActivity.objects.get(activity_id=id)
	context = {}
	context["Activity"] = 
	return render(request,"Activities/details.html", context)
