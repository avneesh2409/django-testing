from django.db import models

# Create your models here.


class RegisterModel(models.Model):
    FullName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    email = models.EmailField()


class School(models.Model):
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students")

    def __str__(self):
        return self.name
