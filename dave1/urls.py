
from django.urls import path
from . import views 

urlpatterns = [
   
    path('',views.index,name="index"), 
    path('about',views.about,name="index"), 
    path('services',views.services,name="services"), 
    path('contact',views.contact,name="contact"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    # path('',views.index,name="home"),
]

   

