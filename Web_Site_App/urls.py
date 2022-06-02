from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('About_us/', views.About_us, name='about'),
    path('Create/', views.Create, name='create'),
    path('Delete/', views.Delete, name='delete')
]
