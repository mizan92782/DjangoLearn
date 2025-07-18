from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.Serializer):
  
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  email =serializers.EmailField()
  
  #! ==== create a instance or insert in database
  def create(self,validator_data):
    return Students.objects.create(**validator_data)
  
  
  
  #! ========= update instance data
  def update(self,instance,validate_data):
    instance.name = validate_data.get('name',instance.name)
    instance.age = validate_data.get('age',instance.age)
    instance.email = validate_data.get('email',instance.email)
    
    #save instace
    instance.save()
    # return data
    return instance
    
    