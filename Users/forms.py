from django import forms
from django.db import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(UserForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = User

		password = forms.CharField(widget=forms.PasswordInput)
		
		widgets = {
			'password': forms.PasswordInput()
		}

		fields = ('username', 'email', 'password', 'first_name', 'last_name')