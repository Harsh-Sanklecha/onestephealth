from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctors, name ="doctors"),
    path('consult/', views.consult, name ="consult"),
    path('diagnosis/', views.diagnosis, name ="diagnosis"),
    path('vijaya/', views.personalDiag, name ="personalDiag"),
    path('sujata/', views.personalDoc, name ="personalDoc"),

]