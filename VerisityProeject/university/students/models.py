from django.db import models
from django.forms import ValidationError

# Create your models here.
class Student(models.Model):
    """
    Model representing a student.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    batch = models.CharField(max_length=10)
    
    #! This method returns a string representation of the model instance.
    #!without this,it shows as object in admin interface
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    