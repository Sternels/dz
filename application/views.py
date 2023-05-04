from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.http import JsonResponse

from .models import CreditPipeline


class IndexView(TemplateView):
    template_name = 'index.html'


class TrainedModelAPIView(APIView):

    def post(self, request, *args, **kwargs):

        total_income = float(request.data.get("salary")) + float(request.data.get("spouse_salary"))
        monthly_income = total_income - float(request.data.get("expenses"))

        mp_cnt = int(request.data.get("loan_term")) * 12
        r = float(request.data.get("interest_rate")) / 1200.0
        ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
        mp = float(request.data.get("loan_amount")) * ak
        total = mp * mp_cnt

        if monthly_income < mp:
            result = False
        else:
            result = True

        credit_pipeline = CreditPipeline(
            result=result,
            expenses=int(request.data.get("expenses")),
            income=int(total_income),
            salary=float(request.data.get("salary")),
            spouse_salary=float(request.data.get("spouse_salary")),
            pasport=request.data.get("pasport"),
            snils=request.data.get("snils"),
            inn=request.data.get("inn"),
            loan_amount=float(request.data.get("loan_amount")),
            loan_term=mp_cnt,
            interest_rate=float(request.data.get("interest_rate")),
            monthly_payment=float(mp),
            main_sum=float(total)
        )
        credit_pipeline.save()
        location_dict = {
            'result': result,
            'expenses': int(request.data.get("expenses")),
            'income': int(total_income),
            'salary': float(request.data.get("salary")),
            'spouse_salary': float(request.data.get("spouse_salary")),
            'pasport': request.data.get("pasport"),
            'snils': request.data.get("snils"),
            'inn': request.data.get("inn"),
            'loan_amount': float(
                request.data.get("loan_amount")),
            'loan_term': int(
                request.data.get("loan_term")),
            'interest_rate': float(
                request.data.get("interest_rate")),
            'monthly_payment': float(mp),
            'main_sum': float(total)
        }
        return Response(location_dict, status=status.HTTP_200_OK)
