from django.contrib import admin
from django.urls import path, include
from . import views
from .views import activity_log_view


urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('activity_log', views.activity_log_view, name='activity_log'),
    path('signout', views.signout, name="signout"),
    path('index',views.index,name="index"),
    
    path('',views.index),
    path('',views.signin),
    path('',views.signup),
    path('',views.activity_log_view),


    
]