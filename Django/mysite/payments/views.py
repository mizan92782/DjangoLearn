from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import payments
from payments.models import Name

def homepage(request):
    
    dic={'friends':['Ratul', 'Shuvo', 'Sakib', 'Sabbir', 'Sami']}
    return render(request, 'payments/payment_home.html',dic)

def bkash(request):
    return render(request, 'payments/bkash.html')
def nagad(request):
    return HttpResponse("<h1>nagad</h1>")

def upai(request):
    return HttpResponse("<h1>upai</h1>")


def payments_method(request):
    pay_m=Name.objects.all();
    return render(request, 'payments/payMethod.html',{'pay':pay_m})