from django.urls import path
from . import views

urlpatterns = [
    #path('documents/', views.documents, name='documents'),
    path('accueil-dgt', views.homeDgt, name="homedgt"),
    path('dgt/', views.dgt, name='dgt'),
    path('dgt-dashboard/', views.dgtDashboard, name='dgtdashboard'),
    path('edit-dgt/<int:pk>', views.editDgt, name='editdgt'),
    path('delete-dgt/<int:pk>', views.deleteDgt, name='deletedgt'),

    #Nouveau
    
    path('ajouter-dgt-category', views.addCategory, name="add-dgt-category"),
    path('edit-dgt-ecategory/<int:pk>', views.editCategory, name='editdgtcategory'),

    path('delete-category/<int:pk>', views.deleteCategory, name='delete-dgt-category'),
    path('category/<str:cats>/', views.CategoryView, name="category"),


    path('detail-dgt/<str:slug>', views.detailDgt, name="detail-dgt"),
    
]