from django.urls import path
from . import views

urlpatterns = [
    path('actualites/', views.actualites, name='actualites'),
    path('actualitesmeps/', views.actu, name='actu'),
    path('editactualite/<int:pk>', views.editactualites, name='editactualites'),
    path('deleteactualite/<int:pk>', views.deleteActualites, name='deleteactualite'),
    path('detail/<str:slug>', views.blog_detail, name="blog_detail"),
]