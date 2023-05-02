from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class ApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application'
    path = os.path.join(settings.MODELS, 'model.pkl')
    with open(path, 'rb') as pickled:
       data = pickle.load(pickled)
    logistic_regression = data