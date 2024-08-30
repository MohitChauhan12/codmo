from django.shortcuts import render,redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
	return render(request,'index.html',{})

def about(request):
	return render(request,'about.html',{})

def post(request):
	return render(request,'post.html',{})

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		form_Frist=form.cleaned_data.get("Frist_name")
		form_last=form.cleaned_data.get("Last_name")
		form_email=form.cleaned_data.get("Your_Email")
		form_mobile=form.cleaned_data.get("Mobile_NO")
		form_commant=form.cleaned_data.get("comment")

		subject="Testing Mail"
		from_email=settings.EMAIL_HOST_USER
		to_email=[from_email,form_email]
		contact_message="%s: %s: %s: %s: via %s"%(

		form_Frist,
		form_last,
		form_mobile,		
		form_commant,
		form_email
		)

		try:
			send_mail(subject,contact_message,from_email,to_email)
		except BadHeaderError:
			return HttpResponse("Invalid header found.")
		return redirect("success")

	context={"form":form,}
	return render(request,"form.html",context)


def success(request):
	return render(request,"success.html")