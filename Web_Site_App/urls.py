from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Hello/', views.Hello),
    path('About_us/', views.About_us)
]
