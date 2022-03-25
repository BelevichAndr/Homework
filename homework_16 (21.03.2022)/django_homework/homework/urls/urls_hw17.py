from django.contrib import admin
from django.urls import path, include
from homework.views import *

urlpatterns = [
    path("", main_hw_17),
    path("first/", first_hw17, name="first_hw17"),
    path("auto_first/", auto_first_hw17, name="auto_first_hw17"),
    path("add_customer/", add_customer, name="add_customer"),
]


