from django.conf.urls import url
from .views import *



urlpatterns = [
    url('^$', index , name= "index"),
    url('^home/',home,name = "home"),
    url('^about/',about,name="about"),
    url('^event/',event,name="event"),
    url('^contact/',contact,name="contact"),
    url('^register/',register,name="register"),
    url('^users/',users,name="users"),
]
