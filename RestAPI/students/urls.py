
import django.urls 
from django.urls import include, path
from . import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')


  

urlpatterns=[
  path('', include(router.urls)),
  path('api/',views.getByApi, name='getByApi'),
  path('<int:pk>/',views.studentInfoPK, name='studentInfoPK'),
  path('create/',views.createStudent.as_view(), name='createStudent'),
  path('mixin/<int:pk>/',views.StudentMixin.as_view(), name='mixin'),
  path('create/<int:pk>/',views.createStudent.as_view(), name='createStudent'),
  
]