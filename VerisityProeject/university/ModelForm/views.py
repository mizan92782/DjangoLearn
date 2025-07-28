import django
from django.shortcuts import render
from .models import People
from .forms import PeopleForm  # Import PeopleForm from the forms module

# Create your views here.

def Peopleview(request):
  context={}
  context['form'] = PeopleForm(request.POST or None)  # Initialize the form with POST data if available
  return render(request, 'fromhtml.html',context)