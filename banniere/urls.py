from django.urls import path
from . import views

urlpatterns = [
    path('add_banner/', views.add_banner, name='add-banner'),
    path('edit-banner/<int:pk>', views.editbanner, name='edit-banner'),
    path('add_photo/', views.add_photo, name='add-photo'),

    path('edit-photo/<int:pk>', views.editPhoto, name='editphoto'),
    path('delete-photo/<int:pk>', views.deletePhoto, name='deletephoto'),
]