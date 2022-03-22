from django.contrib import admin
from django.urls import path
from homework.views import *

urlpatterns = [
    path("first/", first),
    path("second/", second),
    path("third/", third),
    path("sixth/", sixth),
]
