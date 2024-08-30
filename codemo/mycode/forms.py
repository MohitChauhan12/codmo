from django import forms

class ContactForm(forms.Form):
	Frist_name=forms.CharField(required=True)
	Last_name=forms.CharField(required=True)
	Your_Email=forms.EmailField(required=True)
	Mobile_NO=forms.IntegerField(required=True)
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols':23}))