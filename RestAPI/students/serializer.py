from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.Serializer):
  
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  email =serializers.EmailField()
  
  #! ==== create a instance or insert in database
  def create(self,validator_data):
    return Students.objects.create(**validator_data)
    