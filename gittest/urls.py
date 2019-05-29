from django.urls import path
from gittest import views

urlpatterns = [
    path('', views.index),
]
