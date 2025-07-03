from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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
    