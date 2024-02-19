from django.urls import path
from . import views

urlpatterns = [

    path('faq/', views.faq, name='faq'),
    path('edit-faq/<int:pk>', views.editFaq, name='editfaq'),
    path('delete-faq/<int:pk>', views.deleteFaq, name='deletefaq'),
    path('detail-faq/<str:slug>', views.detailFaq, name="detail-faq"),

]