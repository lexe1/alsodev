from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('list/', views.list, name='list'),
    path('details/<str:pk>/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
