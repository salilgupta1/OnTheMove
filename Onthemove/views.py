from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def home_page(request):
	return render(request,'Onthemove/index.html')
