from django.urls import path
from .views import HomeWorkView

urlpatterns = [
    path('get/', HomeWorkView.as_view(), name="hw20_get"),
    path('post/', HomeWorkView.as_view(), name="hw20_post"),
]