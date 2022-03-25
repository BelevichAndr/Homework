from django.contrib import admin
from django.urls import path, include
from homework.views import *

urlpatterns = [
    path("", main_hw_16),
    path("first/", first_hw16),
    path("second/", second_hw16),
    path("third/", third_hw16),
    path("sixth/", sixth_hw16),
]