from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import DefineUserForm

# Create your views here.
def authentication_form(request):
   if request.method == 'POST':
     frm= UserCreationForm(request.POST)
     if frm.is_valid():
       frm.save()
       # Optionally, redirect to a success page or login page
       #return render(request, 'authentication/success.html')
   else:
      frm=UserCreationForm()
  
    
   return render(request, 'authentication/authentication.html',{'form': frm})



def DefineAuthForm(request):
   if request.method=='POST':
      frm = DefineUserForm(request.POST)
      if frm.is_valid():
         frm.save();
         print("user crated succedfully")
   else:
      frm = DefineUserForm()
      print("user not created")
   return render(request, 'authentication/define_auth.html', {'form': frm})