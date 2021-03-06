from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from Activities.models import OnthemoveActivity
from django.http import HttpResponseRedirect,HttpResponse
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf
import json

@ensure_csrf_cookie
def home_page(request):
	if request.is_ajax():
		lat = request.POST['coords[lat]']
		lng = request.POST['coords[lng]']
		request.session['cur_lat'] = lat;
		request.session['cur_lng'] = lng;
		return HttpResponse("Thanks!")
	else:
		act = OnthemoveActivity.objects.select_related('location_id').filter(is_closed=False)
		coordinates =[]
		act_json = serializers.serialize('json',act,fields = ('activity_name','location_id'))
		for i in act:
			coordinates.append(serializers.serialize('json',[i.location_id],fields = ('latitude','longitude')))
		context = {}
		context['activity_info']=act_json
		context['location_info']= coordinates
		context['time_path']=request.path + "time/"
		context['path'] = request.path
		context.update(csrf(request))
		return render(request,'Onthemove/index.html',context)

def time_query(request):
	if request.is_ajax():
		act = OnthemoveActivity.objects.filter(date__range=[request.POST.get("start"), request.POST.get("end")]).filter(is_closed=False)
		coordinates =[]
		act_json = serializers.serialize('json',act,fields = ('activity_name','location_id'))
		for i in act:
			coordinates.append(serializers.serialize('json',[i.location_id],fields = ('latitude','longitude')))
		response = {}
		response['activity_info'] = act_json
		response['location_info'] = coordinates
		return HttpResponse(json.dumps(response), content_type="application/json")
