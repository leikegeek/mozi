from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.json, name='json'),
    path('home/', views.home, name='home'),
]