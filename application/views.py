from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import statsmodels.api as sm

from .apps import ApplicationConfig
from .models import CreditPipeline


class IndexView(TemplateView):
    template_name = 'index.html'


class TrainedModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        dct = {k: [v] for k, v in request.data.items()}
        df = pd.DataFrame(dct)
        df = df.drop(["home", "job", "marital", "records", "savings"],axis=1)
        print(df)
        result = ApplicationConfig.logistic_regression.predict( sm.add_constant( df ) )
        credit_pipeline = CreditPipeline(request.data)
        # credit_pipeline.save()
        return Response({"result": result})
