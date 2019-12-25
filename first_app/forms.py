from django import forms
from .models import RegisterModel, Student


class RegisterForm(forms.ModelForm):

    class Meta():
        model = RegisterModel
        fields = "__all__"


class StudentForm(forms.ModelForm):

    class Meta():
        model = Student
        fields = "__all__"
