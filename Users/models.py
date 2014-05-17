from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField 
# Create your models here.

class OnthemoveUser(models.Model):
	user = models.OneToOneField(User)
	MALE = "M"
	FEMALE = "F"
	PNT = "NA"
	GENDER = (
		(MALE,"Male"),
		(FEMALE,"Female"),
		(PNT,"Prefer not to Disclose"))
	gender = models.CharField(max_length=2,choices = GENDER,default =PNT )
	phoneNumber = PhoneNumberField(blank=True)
	img = models.ImageField(upload_to ="static/Users/img/user_img",default="static/Users/img/user_img/default_user.jpg",null=True)
	age = models.IntegerField(null=True,blank=True)