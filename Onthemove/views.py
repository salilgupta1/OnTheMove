from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from Activities.models import OnthemoveActivity
from django.core import serializers
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
		act = OnthemoveActivity.objects.select_related('location_id').all()
		coordinates =[]
		act_json = serializers.serialize('json',act,fields = ('activity_name','location_id'))
		for i in act:
			coordinates.append(serializers.serialize('json',[i.location_id],fields = ('latitude','longitude')))
		context = {}
		context['activity_info']=act_json
		context['location_info']= coordinates
		context['path'] = request.path
		return render(request,'Onthemove/index.html',context)

def current_location(request):
	if request.is_ajax():
		lat = request[0]
		lng = request[1]
		request.session['cur_lat'] = lat;
		request.sessing['cur_lng'] = lng;
		return HttpResponse("Thanks!")
