
from django.urls import path

from authentication import views


urlpatterns = [
    path('home/',views.homepage ,name='homepage'),  
    path('login/',views.loginUser ,name='login'),  
    path('about/',views.about ,name='about'),  
]

