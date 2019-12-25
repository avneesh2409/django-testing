from django.shortcuts import render
from .forms import RegisterForm
from .models import RegisterModel
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
	title = "My First Web App"	
	return render(request,'index.html',{'title':title})

def home(request):
	title = "home"
	return render(request,'home.html',{'title':title})
def about(request):
	title = "about"
	return render(request,'about.html',{'title':title})

def event(request):
	title = "event"
	return render(request,'event.html',{'title':title})

def contact(request):
	title = "contact"
	return render(request,'contact.html',{'title':title})

def register(request):
	forms = RegisterForm()
	title = "register here"
	if request.method == 'POST':
		forms = RegisterForm(request.POST)
		if forms.is_valid():
			forms.save(commit=True)
			return HttpResponseRedirect('/first_app')
		else:
			print("invalid form")
	return render(request,'register.html',{'title':title,'form':forms})