from django.urls import path
from . import views

urlpatterns = [
    #path('documents/', views.documents, name='documents'),
    path('accueil-dge', views.homeDge, name="homedge"),
    path('dge/', views.dge, name='dge'),
    path('dge-dashboard/', views.dgeDashboard, name='dgedashboard'),
    path('edit-dge/<int:pk>', views.editDge, name='editdge'),
    path('delete-dge/<int:pk>', views.deleteDge, name='deletedge'),

    #Nouveau
    
    path('ajouter-dge-category', views.addCategory, name="add-dge-category"),
    path('edit-dg-ecategory/<int:pk>', views.editCategory, name='editdgecategory'),

    path('delete-category/<int:pk>', views.deleteCategory, name='delete-dge-category'),
    path('category/<str:cats>/', views.CategoryView, name="category"),


    path('detail-dge/<str:slug>', views.detailDge, name="detail-dge"),
    
]