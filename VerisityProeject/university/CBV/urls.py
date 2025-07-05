import django.urls


from . import views

urlpatterns=[
  django.urls.path('',views.simpleCBV.as_view(), name='simple_cbv'),
  django.urls.path('templete/',views.templeteCVB.as_view(), name='templete_cbv'),
  django.urls.path('redirect/', views.DynamicRedirectView.as_view(), name='dynamic_redirect'),
  django.urls.path('createview/', views.FriendsCreateView.as_view(), name='create_view'),
  django.urls.path('listview/', views.FriedsListView.as_view(), name='list_view'),
  django.urls.path('<pk>/update/', views.FriendsUpdateView.as_view(), name='update_view'),
  
  
]