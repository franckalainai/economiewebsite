from django.urls import path
from . import views

urlpatterns = [
    #path('documents/', views.documents, name='documents'),
    path('budget/', views.budget, name='budget'),
    path('documents/', views.documents, name='documents'),
    path('budgets-meps/', views.budgetsMeps, name='budgetsmeps'),
    path('budgets-dashboard/', views.budgetsEtatDashboard, name='budgetsdashboard'),
    path('edit-budget/<int:pk>', views.editaBudgets, name='editbudget'),
    path('delete-budget/<int:pk>', views.deleteBudgets, name='deletebudget'),

    path('etat-budget-meps/', views.EtatBudgetsMeps, name='etatexecutionbudget'),
    path('etat-budget/', views.etatBudget, name='etat-budget'),
    path('edit-etat-budget/<int:pk>', views.editEtatBudget, name='editetatbudget'),
    path('delete-etat-budget/<int:pk>', views.deleteEtatBudget, name='deleteetatbudget'),

    #Nouveau
    
    path('ajouter_category', views.addCategory, name="add_category"),
    path('edit-category/<int:pk>', views.editCategory, name='editcategory'),

    path('delete-category/<int:pk>', views.deleteCategory, name='deletecategory'),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    
]