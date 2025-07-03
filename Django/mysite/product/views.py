from django.http import HttpResponse
from django.shortcuts import render
from product.forms import productForm, productForm

# Create your views here.

def Cake(request):
  return HttpResponse('cake is ready')

def FromsView(request):
  frm=productForm()
  frm.order_fields(field_order=sorted(frm.fields.keys()))
  return render(request, 'product/productform.html', {'form': frm})