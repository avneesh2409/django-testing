from django.shortcuts import render
from .forms import RegisterForm,StudentForm,SchoolForm
from .models import RegisterModel, School
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
# Create your views here.


class SchoolListView(ListView):
    model = School
    template_name = 'school_list.html'

def student(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
	return render(request,'student.html',{'form':form,'title':'student Register'})

def schools(request):
	form = SchoolForm()
	if request.method == 'POST':
		form = SchoolForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
	return render(request,'schools.html',{'form':form,'title':'school Registration'})


class StudentDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'detail.html'


def index(request):
    title = "My First Web App"
    return render(request, 'index.html', {'title': title})


def home(request):
    title = "home"
    return render(request, 'home.html', {'title': title})


def about(request):
    title = "about"
    return render(request, 'about.html', {'title': title})


def event(request):
    title = "event"
    return render(request, 'event.html', {'title': title})


def contact(request):
    title = "contact"
    return render(request, 'contact.html', {'title': title})


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
    return render(request, 'register.html', {'title': title, 'form': forms})


def users(request):
    users = RegisterModel.objects.all()
    return render(request, 'users.html', {'users': users, 'title': 'show users'})
