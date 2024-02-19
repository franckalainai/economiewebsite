from django.urls import path
from . import views

urlpatterns = [
    path('zoom/', views.zoom, name='zoom'),
    path('zooms/', views.zooms, name='zooms'),
    path('editzoom/<int:pk>', views.editzoom, name='editzoom'),
    path('deletezoom/<int:pk>', views.deletezoom, name='deletezoom'),
    path('detail-zoom/<str:slug>', views.detail_zoom, name="detail-zoom"),
]