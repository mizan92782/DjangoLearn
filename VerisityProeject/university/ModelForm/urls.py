import django.urls
from django.urls import path
from .views import Peopleview

urlpatterns=[
  path('', Peopleview, name='people_view'),
  path('one/', Peopleview, name='people_view'),
  path('two/', Peopleview, name='people_view'),
]