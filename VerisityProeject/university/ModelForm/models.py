from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(required=True)
    address = models.TextField()
    

    def __str__(self):
        return self.name