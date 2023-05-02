from django.urls import path

from .views import *

app_name = 'application'

urlpatterns = [
    path("check/", TrainedModelAPIView.as_view()),
]