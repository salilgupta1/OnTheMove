from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Activities.models import OnthemoveActivity
from django.core import serializers
import json

def home_page(request):
	act = OnthemoveActivity.objects.select_related('location_id').all()
	coordinates =[]
	act_json = serializers.serialize('json',act,fields = ('activity_name','location_id'))
	for i in act:
		coordinates.append(serializers.serialize('json',[i.location_id],fields = ('latitude','longitude')))
	context = {}
	context['activity_info']=act_json
	print context['activity_info']
	context['location_info']= coordinates
	return render(request,'Onthemove/index.html',context)
