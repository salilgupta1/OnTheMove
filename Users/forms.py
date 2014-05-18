from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from models import OnthemoveUser
from localflavor.us.models import PhoneNumberField 

class UserForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(UserForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})
		self.fields["email"].required = True

	class Meta:
		model = User

		password = forms.CharField(widget=forms.PasswordInput)
		email = forms.EmailField(required=True)

		widgets = {
			'password': forms.PasswordInput()
		}

		fields = ('first_name', 'last_name', 'email', 'password')

class OnthemoveUserForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(OnthemoveUserForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = OnthemoveUser

		MALE = "M"
		FEMALE = "F"
		PNT = "NA"
		GENDER = (
			(MALE,"Male"),
			(FEMALE,"Female"),
			(PNT,"Prefer not to Disclose"))
	 	gender = forms.ChoiceField(choices = GENDER)
		phoneNumber = PhoneNumberField()
		age = forms.IntegerField()
		fields = ('gender','phoneNumber', 'age')

class OnthemoveUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=15,error_messages={'required':'Please input a username'}, widget = forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}),error_messages = {'required':'Please Input a password'})