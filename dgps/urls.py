from django.urls import path
from . import views

urlpatterns = [
    #path('documents/', views.documents, name='documents'),
    path('accueil-dgps', views.homeDgps, name="homedgps"),
    path('dgps/', views.dgps, name='dgps'),
    path('dgps-dashboard/', views.dgpsDashboard, name='dgpsdashboard'),
    path('edit-dgps/<int:pk>', views.editDgps, name='editdgps'),
    path('delete-dgps/<int:pk>', views.deleteDgps, name='deletedgps'),

    #Nouveau
    
    path('ajouter-dgps-category', views.addCategory, name="add-dgps-category"),
    path('edit-dgps-ecategory/<int:pk>', views.editCategory, name='editdgpscategory'),

    path('delete-category/<int:pk>', views.deleteCategory, name='delete-dgps-category'),
    path('category/<str:cats>/', views.CategoryView, name="category"),


    path('detail-dgps/<str:slug>', views.detailDgps, name="detail-dgps"),
    
]