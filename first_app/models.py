from django.db import models

# Create your models here.

class RegisterModel(models.Model):
	FullName = models.CharField(max_length=100)
	Password = models.CharField(max_length=100)
	email = models.EmailField()