from django.db import models

# Create your models here.
class Name(models.Model):
    pai_id = models.IntegerField()
    pay_option = models.CharField(max_length=100)
    min_pay = models.IntegerField()

     
