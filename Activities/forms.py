from django import forms
from models import OnthemoveActivity,OnthemoveLocation

class ActivityForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(ActivityForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
				fields[1].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = OnthemoveActivity
		fields = ['activity_name','start_time','end_time','max_num_attendees','min_num_attendees','skill_level','date']
