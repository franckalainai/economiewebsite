from django.urls import path
from . import views

urlpatterns = [
    #path('documents/', views.documents, name='documents'),
    path('direction/', views.direction, name='direction'),
    path('direction-dashboard/', views.directionDashboard, name='directiondashboard'),
    path('edit-direction/<int:pk>', views.editdirection, name='editdirection'),
    path('delete-direction/<int:pk>', views.deletedirection, name='deletedirection'),

    #Nouveau
    
    path('ajouter-direction-category', views.addCategory, name="add-direction-category"),
    path('edit-direction-ecategory/<int:pk>', views.editCategory, name='editdirectioncategory'),

    path('delete-category/<int:pk>', views.deleteCategory, name='delete-direction-category'),
    path('category/<str:cats>/', views.CategoryView, name="category"),


    path('accueil-direction', views.homedirection, name="homedirection"),
    path('detail-direction/<str:slug>', views.detaildirection, name="detail-direction"),
    
]