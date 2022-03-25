from django.contrib import admin
from django.urls import path, include
from homework.views import main_page

urlpatterns = [
    path('', main_page, name="main_page"),
    path('homework_16/', include("homework.urls.urls_hw16")),
    path('homework_17/', include("homework.urls.urls_hw17")),

]
