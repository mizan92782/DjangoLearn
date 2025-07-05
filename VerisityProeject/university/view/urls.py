from django.urls import include, path
from . import views
urlpatterns=[
  path('', views.Viewsall, name='viewsall'),  
  path('<int:view_id>/', views.ViewsSearch, name='viewsearch'),  
  path('<int:view_id>/update', views.ViewsUpdate, name='viewsupdate'),  
]