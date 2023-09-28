from django.urls import path 
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import *

urlpatterns =[
    path('login/',LoginView.as_view(),name='baselogin'),
    path('',views.home,name='home'),
    path('logout/',LogoutView.as_view(),name='baselogout'),
    path('Good-bye/',views.bye,name='Goodbye'),
    path('home/',views.welcome,name = 'welcome'),
    path('register/',views.register_request,name='registerpage'),
    path('form/',test_form.as_view(),name = 'oo'),
]