
import django.urls 
from django.urls import path
from . import views

urlpatterns=[
  path('',views.studentInfo, name='studentInfo'),
  path('api/',views.getByApi, name='getByApi'),
  path('<int:pk>/',views.studentInfoPK, name='studentInfoPK'),
  
]