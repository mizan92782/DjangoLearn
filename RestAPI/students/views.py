import django.http
from urllib import request
from django.shortcuts import render
from .serializer import StudentsSerializer
from .models import Students

from rest_framework.renderers import JSONRenderer
import requests
# Create your views here


#! get all object : crate a api for database;
# ! by using this database data can be accessed by any client
def studentInfo(request):
    # complex data : get use for all object
    students= Students.objects.all()
    # simple native python data
    # many for multiple object
    serializer= StudentsSerializer(students, many=True)
    # render to json
    data = JSONRenderer().render(serializer.data)


    return django.http.HttpResponse(data, content_type='application/json')



# ! this function show how can we get data from external api or urls
def getByApi(request):
    #! 1. hit api url
    URL="https://reqres.in/api/users?page=2"

    #! 2. get response : data
    response = requests.get(url=URL)



    #! 3. extract data from response
    data=response.json()

    #! 4. show and print data
    print(data)
    
    return django.http.JsonResponse(data)




#! get all object
def studentInfoPK(request,pk):
    #complex data : get use for sigle object
    students=Students.objects.get(pk=pk)
    
    # simple native python data
    # many for multiple object
    serializer=StudentsSerializer(students)
    
    # render to json
    student_json= JSONRenderer().render(serializer.data)
    
    return django.http.HttpResponse(student_json, content_type='application/json')