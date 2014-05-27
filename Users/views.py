from django.shortcuts import render
from forms import UserForm, OnthemoveUserForm
from Activities.models import OnthemoveActivity
from Users.models import OnthemoveUser
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.core.context_processors import csrf
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.urlresolvers import reverse
#from django import forms
#for mail
from django.core.mail import EmailMessage
  

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

			#send_mail(subject,message,from_email,to_list,fail_silently = True )
			# subject = 'You have registered for OnTheMove'
			# message = 'Thank you for registering OnTheMove.\n'
			# from_email = settings.EMAIL_HOST_USER
			# to_list = [settings.EMAIL_HOST_USER]

			# send_mail(subject,message,from_email,to_list,fail_silently = True)
			# msg = EmailMultiAlternatives(subject, message, from_email,to)
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()
			email = onthemove_user.user.email
			msg = EmailMessage('You have registered for OnTheMove','Hi '+ new_user.first_name+',\nThank you for registering OnTheMove!',from_email = 'noreply@onthemove.com',to = [email])
			msg.send()
			return HttpResponseRedirect(reverse('Users:login'))
	else:
		userForm = UserForm()
		onthemoveUserForm = OnthemoveUserForm()
	context = {}
	context["userForm"] = userForm
	context["onthemoveUserForm"] = onthemoveUserForm

	return render(request,"Users/createUser.html", context)
@login_required
def my_activity(request):
	user = request.user.onthemoveuser
	enrolled = user.a.all()
	pending = user.pa.all()
	own = user.o.all()
	context = {}
	context['enrolled'] = enrolled
	context['pending'] = pending
	context['own'] = own
	return render(request,'Users/myActivities.html',context)
@login_required
def my_participants(request,act_id):
	act = OnthemoveActivity.objects.get(pk=act_id)
	context = {} 
	context['act_id']=act_id
	if request.method =='POST':
		message = request.POST.get('message')
		if len(message):
			subject = request.POST.get('subject')
			if not len(subject):
				subject ='Onthemove Owner of '+act.activity_name+' sent a message'
			from_email = "noreply@onthemove.com"
			html_content = get_template('Users/participantEmail.html').render(
				Context({
					"message":message
				})
			)	
			to = [x.user.email for x in act.attendees.all()]
			to.append(request.user.email)
			msg = EmailMultiAlternatives(subject, message, from_email,to)
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			context['success']= "Your email has been sent!"
		else:
			context['error_message'] ="You didn't type a message!"
	attendees = act.attendees.all()
	context['name'] = act.activity_name
	context['attendees'] = attendees
	context.update(csrf(request))
	return render(request,'Users/viewParticipants.html',context)



