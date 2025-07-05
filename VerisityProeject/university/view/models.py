from django.db import models

# Create your models here.

class Views(models.Model):
  view_id = models.AutoField(primary_key=True)
  title= models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  time=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.view_id} {self.title}"

    

    