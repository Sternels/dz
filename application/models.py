from django.db import models


class CreditPipeline(models.Model):
    status = models.CharField(max_length=100)
    seniority = models.IntegerField()
    home = models.CharField(max_length=100)
    time = models.IntegerField()
    age = models.IntegerField()
    marital = models.CharField(max_length=100)
    records = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    expenses = models.IntegerField()
    income = models.IntegerField()
    assets = models.IntegerField()
    debt = models.IntegerField()
    amount = models.IntegerField()
    price = models.IntegerField()
    finrat = models.DecimalField(max_digits=12, decimal_places=9)
    savings = models.DecimalField(max_digits=12, decimal_places=9)
    pasport = models.IntegerField()
    snils = models.IntegerField()
    inn = models.IntegerField()

    def __str__(self):
        return self.status
