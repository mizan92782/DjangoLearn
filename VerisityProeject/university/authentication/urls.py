import django.urls
from . import views
urlpatterns = [
  django.urls.path('', views.authentication_form, name='auth_form'),
  django.urls.path('dauth', views.DefineAuthForm, name='define_auth_form'),
  ]