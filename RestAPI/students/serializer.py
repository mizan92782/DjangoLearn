from rest_framework import serializers

class StudentsSerializer(serializers.Serializer):
  
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  email =serializers.EmailField()