from django.urls import path
from . import views
import product


urlpatterns = [
    path('', views.FromsView),
    
]
