from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.age}) - {self.email}"
    
    
    
    
    class Meta:
        #for showing order
        ordering = ['name']
