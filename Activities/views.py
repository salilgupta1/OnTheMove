from django.shortcuts import render
from forms import ActivityForm
from django.core.context_processors import csrf
# Create your views here.

def details(request):
	return render(request,'Activities/details.html')

def create_Activity(request):
	if request.method == 'POST':
		form = ActivityForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("Ontehmove:index"))
	else:
		form = ActivityForm()
	context = {}
	context.update(csrf(request))
	context['create_form'] = form
	return render(request,"Activities/createActivity.html",context)