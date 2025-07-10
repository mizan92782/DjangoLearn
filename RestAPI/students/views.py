import io
import django.http
from urllib import request
from django.shortcuts import render
from .serializer import StudentsSerializer
from .models import Students

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import requests
from django.views.decorators.csrf import csrf_exempt
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




#! get  by pk object
def studentInfoPK(request,pk):
    #complex data : get use for sigle object
    students=Students.objects.get(pk=pk)
    
    # simple native python data
    # many for multiple object
    serializer=StudentsSerializer(students)
    
    # render to json
    student_json= JSONRenderer().render(serializer.data)
    
    return django.http.HttpResponse(student_json, content_type='application/json')




#! ==== create a new student : creae api for add data in database
''' csrf : token must be decorate'''


@csrf_exempt
def createStudent(request):
    if request.method == 'POST':
        # get json data from request
        json_data = request.body
        
        # convert json data to stream
        stream = io.BytesIO(json_data)
        
        # stream to python data
        python_data = JSONParser().parse(stream)
        
        
        # ptocess the data using serializer
        serializer = StudentsSerializer(data=python_data)
        
        
        # validation data
        if serializer.is_valid():
            
            # save data in database
            serializer.save()
            res={
                'msg': 'Data created successfully',
                'data': serializer.data
            }
            
            json_data = JSONRenderer().render(res)
            return django.http.HttpResponse(json_data, content_type='application/json')
        
        # show error if not valid
        json_data= JSONRenderer().render(serializer.errors)
        return django.http.HttpResponse(json_data, content_type='application/json', status=400)
    
    return django.http.HttpResponse("request")  # Method Not Allowed for non-POST requests