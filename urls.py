
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('contact', views.contact),
    path('help', views.help),
    path('lessons', views.lesson),
    path('newsletter', views.newsletter),
    path('calendar', views.calendar),
    path('test', views.test),
    path('count/', views.count, name='count'),
]
