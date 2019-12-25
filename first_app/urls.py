from django.conf.urls import url
from .views import *


app_name = "first_app"

urlpatterns = [
    url('^school_list/(?P<pk>[-\w]+)/$',
        StudentDetailView.as_view(), name='detail'),
    url('^school_list/', SchoolListView.as_view(), name="school_list"),
    url('^$', index, name="index"),
    url('^home/', home, name="home"),
    url('^about/', about, name="about"),
    url('^event/', event, name="event"),
    url('^contact/', contact, name="contact"),
    url('^register/', register, name="register"),
    url('^users/', users, name="users"),
]
