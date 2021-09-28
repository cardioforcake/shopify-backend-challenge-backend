from django.urls import path
from . import views

urlpatterns = [
  path('user/<user_id>/delete/<image_id>', views.delete_user_image, name="delete_user_image"),
  path('user/<user_id>', views.get_user_images, name="get_user_images"),
  path('all', views.get_all_images, name="get_all_images"),
  path('image/<user_id>/add-image', views.add_user_image, name='add_user_image'),
  path('image/add-image', views.add_image, name='add_image'),
  path('', views.test_data, name='test')
]