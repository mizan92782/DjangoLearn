import django.urls
from . import views
urlpatterns = [
  django.urls.path('', views.authentication_form, name='auth_form'),
  ]