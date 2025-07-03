from django.urls import path
from . import views

from students import views


urlpatterns = [
    path('home/', views.home, name='students_home'),  
    path('input/', views.inputStudent, name='input_student'),  
    path('output/', views.outputStudent, name='output_students'),  
    #filter by regex
    path('<int:batch>/', views.studentBatch, name='batch_students'),  
]
