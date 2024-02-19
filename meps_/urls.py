from django.urls import path
from . import views

urlpatterns = [
    path('ministere/', views.ministere, name='ministere'),
    path('directeurs', views.directeurs, name='directeurs'),
    path('edit-ministere/<int:pk>', views.editMinistere, name='editministere'),
    path('delete-ministere/<int:pk>', views.deleteMinistere, name='deleteministere'),
    path('detail-ministere/<str:slug>', views.detailMinistere, name="detail-ministere"),

]