from django.contrib import admin
from django.urls import path
from saude.views import index
urlpatterns = [
    path('',index,name = 'index'),
]