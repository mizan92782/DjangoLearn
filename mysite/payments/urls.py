from django.urls import path
from . import views
import payments


urlpatterns = [
    path('', views.homepage),
    path('bkash/', views.bkash, name='Bkash'),
    path('nagad/', views.nagad ,name='Nagad'),
    path('upai/', views.upai),
    path('paymethod/', views.payments_method, name='paymethod'),
]
