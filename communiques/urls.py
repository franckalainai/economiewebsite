from django.urls import path
from . import views

urlpatterns = [
    path('creer-communique/', views.creerCommunique, name='communique'),
    path('edit-communique/<int:pk>', views.editCommunique, name='editcommunique'),
    path('delete-communique/<int:pk>', views.deleteCommunique, name='deletecommunique'),
    path('communiques/', views.communiques, name='communiques'),
]