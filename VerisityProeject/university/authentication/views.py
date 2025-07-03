import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from .forms import DefineUserForm

# Create your views here.
def authentication_form(request):
   if request.method == 'POST':
     frm= UserCreationForm(request.POST)
     if frm.is_valid():
       frm.save()
       # Optionally, redirect to a success page or login page
       return render(request, 'logout_form')
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




#login form


def login_form(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Submitted username: {username}")
        print(f"Submitted password: {password}")

        frm = AuthenticationForm(request=request,data=request.POST)
        
        if frm.is_valid():
            serName = frm.cleaned_data['username']
            UserPassword = frm.cleaned_data['password']
            user= authenticate(username=serName, password=UserPassword)
           # login(request, user)
            if user is not None:
              login(request, user)
              print("Login successful")
            return redirect('logout_form')  # Replace 'home' with your redirect target
        else:
            print("Login failed")
            #print("Form errors:", frm.errors)
    else:
        frm = AuthenticationForm()
        print("GET request - rendering login form")

    return render(request, 'authentication/login.html', {'form': frm})


#logout
def logout_form(request):
    if request.method == 'POST':
        logout(request)
        print("User logged out successfully")
        # Optionally, redirect to a success page or login page
        return redirect('login_form')
    else:
        print("GET request - rendering logout form")
    
    return render(request, 'authentication/logout.html')  # Adjust the template as needed