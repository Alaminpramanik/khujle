from django.urls import path
 
from . import views
 
urlpatterns = [
   path('create/', views.CategoriesCreateApiView.as_view(), name='categories-create'),
   path('list/', views.CategoriesListApiView.as_view(), name='categories-list'),
   path('update/', views.CategoriesUpdtaeApiView.as_view(), name='categories-update'),
   path('delete/', views.CategoriesDeleteApiView.as_view(), name='categories-create'),
   
   
]
