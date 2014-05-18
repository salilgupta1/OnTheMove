from django.shortcuts import render
from forms import UserForm
from django.http import HttpResponseRedirect

# Create your views here.
def create_user(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			email = request.POST.get('email')
			username = request.POST.get('username')
			password = request.POST.get('password')
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			new_user = form.save()
	else:
		form = UserForm()
	context = {}
	context["form"] = form

	return render(request,"Users/createUser.html", context)
