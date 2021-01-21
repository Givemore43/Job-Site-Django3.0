from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_job/', views.list_job, name='list_job'),
]