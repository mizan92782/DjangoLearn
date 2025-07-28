import io
import django.http
from urllib import request
from django.shortcuts import render
from .serializer import StudentsSerializer
from .models import Students

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

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






class createStudent(APIView):
    def get(self, request, pk=None,format=None):
        if pk is not None:
            #complext data
            student = Students.objects.get(pk=pk)
            # simple native python data
            serializer= StudentsSerializer(student)
            return Response(serializer.data)
    
        else:
            # complex data : get use for all object
            students = Students.objects.all()
            # simple native python data
            # many for multiple object
            serializer = StudentsSerializer(students, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None,format=None):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("a new data insert")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk,format=None):
        student = Students.objects.get(pk=pk)
        serializer = StudentsSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    


#! # Create a mixin for handling student data ap8i
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from .models import Students

class StudentMixin(GenericAPIView, 
                   ListModelMixin, 
                   CreateModelMixin, 
                   UpdateModelMixin, 
                   DestroyModelMixin, 
                   RetrieveModelMixin):

    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)  # For retrieving a single object
        return self.list(request, *args, **kwargs)          # For listing all objects

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)        # Full update

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  # Partial update

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




#!========== model view set,,easy ============
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
