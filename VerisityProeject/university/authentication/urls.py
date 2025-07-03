import django.urls
from . import views
urlpatterns = [
  django.urls.path('', views.authentication_form, name='auth_form'),
  django.urls.path('dauth/', views.DefineAuthForm, name='define_auth_form'),
  django.urls.path('login/', views.login_form, name='login_form'),
  django.urls.path('logout/', views.logout_form, name='logout_form'),
  django.urls.path('password/', views.password_change, name='password_form'),
  ]