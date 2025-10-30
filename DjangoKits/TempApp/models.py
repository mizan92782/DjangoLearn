from django.db import models

# Create your models here.
class Persons(models.Model):
  Name = models.CharField(max_length=20)
  father= models.CharField(max_length=30)
  age= models.IntegerField()
  result= models.FloatField()
  
  