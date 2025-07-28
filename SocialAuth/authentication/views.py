from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login



# Create your views here.

def homepage(request):
    
    return render(request, 'home.html')
  
  
  
@login_required
def about(request):
    return render(request, 'about.html')
  
  
  
from django.contrib.auth.models import User

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Email not registered'})

        # ✅ Authenticate with the found username
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('about')
        else:
            return render(request, 'login.html', {'error': 'Incorrect password'})

    return render(request, 'login.html')


    
 # !*************************** 
from allauth.socialaccount.models import SocialAccount
'''social account model is used to store information about the user's social accounts, such as Google, Facebook, etc.'''
def profile_view(request):
    social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()
    return render(request, 'your_template.html', {
        'social_account': social_account
    })
