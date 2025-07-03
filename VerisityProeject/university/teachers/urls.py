from django.urls import path
from . import views

import django.urls

from teachers import views

urlpatterns =[
  path('home/', views.home, name='teachershome'),
]