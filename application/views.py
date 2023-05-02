from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.generic import TemplateView

from .apps import ApplicationConfig


class IndexView(TemplateView):
    template_name = 'index.html'


class TrainedModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return HttpResponse("sdvsdv")
        

