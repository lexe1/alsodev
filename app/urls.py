from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('list/', views.List, name='list'),
    path('details/<str:pk>/', views.Details, name='details'),
    path('create/', views.Create, name='create'),
    path('update/<str:pk>/', views.Update, name='update'),
    path('delete/<str:pk>/', views.Delete, name='delete'),
]
