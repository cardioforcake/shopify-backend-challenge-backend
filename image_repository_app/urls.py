from django.urls import path
from . import views

urlpatterns = [
  path('image/add_image', views.add_image, name="add_image")
]