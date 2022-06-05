from django.urls import path
from . import views

urlpatterns = [
  path('new/',views.newTask),
  path('all/',views.allTask)
]