from django.urls import path
from utsab.views import home
from . import views

app_name = 'utsab' 


urlpatterns =[
    path("", views.home, name="home"),
    path("contact/", views.user_contact, name="user_contact"),
   
]
