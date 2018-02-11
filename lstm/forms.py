from django import forms

class UpdateForm(forms.Form):
	value = forms.FloatField(label="Today's value")