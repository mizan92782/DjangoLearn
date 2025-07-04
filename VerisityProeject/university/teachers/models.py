from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"