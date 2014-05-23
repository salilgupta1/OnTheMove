from django.db import models
from decimal import Decimal
#from django.contrib.auth.models import User
#from Users.models import OnthemoveUser

# Create your models here.
class OnthemoveActivity(models.Model):
	activity_id = models.AutoField(primary_key=True)
	activity_name =models.TextField(max_length=40,blank=False) 
	start_time = models.TimeField(auto_now=False,null=False)
	end_time = models.TimeField(auto_now=False,null=True)
	location_id = models.ForeignKey('OnthemoveLocation')
	activity_img = models.ImageField(upload_to ="static/Activities/img/activity",default="static/Activities/img/activity/default_act.jpg")
	min_num_attendees = models.IntegerField(null=True, default=1)
	max_num_attendees = models.IntegerField(default=1)
	owner_id = models.ForeignKey("Users.OnthemoveUser",related_name='o')
	attendees = models.ManyToManyField("Users.OnthemoveUser",related_name='a',blank = True)
	pending = models.ManyToManyField("Users.OnthemoveUser",related_name='pa',blank=True)
	BEGINNER = "Beginner"
	INTERMEDIATE = "Intermediate"
	ADVANCED = "Advanced"
	SKILL_LEVEL = (
		(BEGINNER , "Beginner"),
		(INTERMEDIATE, "Intermediate"),
		(ADVANCED ,"Advanced")
	)
	skill_level =models.TextField(max_length=2,choices = SKILL_LEVEL,default =BEGINNER )
	date = models.DateField(null=False)
	is_closed = models.BooleanField(default=False)

class OnthemoveLocation(models.Model):
	location_id = models.AutoField(primary_key=True)
	location_name = models.TextField(max_length=100,blank=False)
	location_img = models.ImageField(upload_to="static/Activities/img/locations",default="static/Activities/img/locations/default_loc.jpg")
	location_img_url = models.URLField(blank=True, null=True)
	location_rate = models.DecimalField(max_digits = 2, decimal_places = 1, default=Decimal('0.0'))
	longitude = models.FloatField('Longitude',null =True, blank = True)
	latitude= models.FloatField('Latitude',null =True, blank = True)
	zipcode = models.IntegerField(null=True)
	address = models.TextField(null=True)
	city = models.TextField(null=True)
	state = models.TextField(null=True)
	country = models.TextField(null=True)
