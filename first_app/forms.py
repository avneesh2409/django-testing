from django import forms
from .models import RegisterModel, School, Student


class RegisterForm(forms.ModelForm):

    class Meta():
        model = RegisterModel
        fields = "__all__"


class SchoolForm(forms.ModelForm):

    class Meta():
        model = School
        fields = "__all__"


class StudentForm(forms.ModelForm):

    class Meta():
        model = Student
        fields = "__all__"
