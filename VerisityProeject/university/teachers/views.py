import django.http
from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Render the home page for the teachers section.
    """
    return django.http.HttpResponse('teachers home')