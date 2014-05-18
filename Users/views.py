from django.shortcuts import render
from forms import UserForm, OnthemoveUserForm
from django.http import HttpResponseRedirect

# Create your views here.
def create_user(request):
	
	if request.method == "POST":
		userForm = UserForm(request.POST)
		onthemoveUserForm = OnthemoveUserForm(request.POST)
		if userForm.is_valid() and onthemoveUserForm.is_valid():
			new_user = userForm.save()

			#hash the password
			new_user.set_password(new_user.password)
			new_user.save()

			#save the OnthemoveUser with the new_user field
			onthemove_user = onthemoveUserForm.save(commit=False)
			onthemove_user.user = new_user
			onthemove_user.save()
			return HttpResponseRedirect('/')
	else:
		userForm = UserForm()
		onthemoveUserForm = OnthemoveUserForm()
	context = {}
	context["userForm"] = userForm
	context["onthemoveUserForm"] = onthemoveUserForm

	return render(request,"Users/createUser.html", context)
