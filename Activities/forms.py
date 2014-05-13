from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from models import OnthemoveActivity,OnthemoveLocation

class ActivityForm(forms.ModelForm):
	activity_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control'}))
	BEGINNER = "Beginner"
	INTERMEDIATE = "Intermediate"
	ADVANCED = "Advanced"
	skill_choices = (
		(BEGINNER , "Beginner"),
		(INTERMEDIATE, "Intermediate"),
		(ADVANCED ,"Advanced")
	)
	skill_level = forms.ChoiceField(choices = skill_choices)
	date = forms.DateField(widget=AdminDateWidget)

	def __init__(self,*args,**kwargs):
		super(ActivityForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
				fields[1].widget.attrs.update({'class':'form-control'})
		
	class Meta:
		model = OnthemoveActivity
		fields = ['activity_name','start_time','end_time','max_num_attendees','min_num_attendees','skill_level','date']
