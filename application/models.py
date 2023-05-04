from django.db import models


class CreditPipeline(models.Model):
    result = models.BooleanField(default=False)
    expenses = models.IntegerField()
    income = models.IntegerField()
    salary = models.FloatField()
    spouse_salary = models.FloatField()
    pasport = models.CharField(max_length=100)
    snils = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    loan_amount = models.FloatField()
    loan_term = models.IntegerField()
    interest_rate = models.FloatField()
    monthly_payment = models.FloatField()
    main_sum = models.FloatField()

    def __str__(self):
        return self.pasport
