from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from . models import *
from .forms import *

# Create your views here.

# Fonctions de gestion des budgets vitrine
def documents(request):
    
    return render(request, 'home/documents/index.html')


def budgetsMeps(request):
    budgets = Budget.objects.all()
    context = {
        'budgets': budgets
    }
    return render(request, 'home/documents/budgets.html', context)

# Fonctions de gestions des formulaires creation/modification/suppression budget

def budgetsEtatDashboard(request):
    
    return render(request, 'accounts/pages/documents/index.html')


def budget(request):
    budgets = Budget.objects.all()

    if request.method == 'POST':
        form = BudgetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('budget')
    else:
        form = BudgetForm()
   
    return render(request, 'accounts/pages/documents/budgets.html', {'form':form,'budgets': budgets})

def editaBudgets(request, pk):

    editBudget = Budget.objects.get(pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST or None, request.FILES,  instance=editBudget)

        if form.is_valid():
            form.save()
            return redirect('budget')
    else:
        form = BudgetForm(instance=editBudget)

    return render(request, 'accounts/pages/documents/budgets.html', {'form': form})

def deleteBudgets(request, pk):

    deleteBudget = Budget.objects.get(pk=pk)
    deleteBudget.delete()

    return redirect('budget')

# Fonctions de creation/modification/suppression etat budget

def etatBudget(request):
    etatsbudgets = EtatBudget.objects.all()

    if request.method == 'POST':
        form = EtatBudgetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('etat-budget')
    else:
        form = EtatBudgetForm()
   
    return render(request, 'accounts/pages/documents/etat_budgets.html', {'form':form,'etatsbudgets': etatsbudgets})

def editEtatBudget(request, pk):

    editEtatBudget = EtatBudget.objects.get(pk=pk)

    editForm = EtatBudgetForm(request.POST or None, instance=editEtatBudget)

    if editForm.is_valid():
        editForm.save()
        return redirect('etat-budget')

    return render(request, 'accounts/pages/documents/etat_budgets.html', {'form': editForm})

def deleteEtatBudget(request, pk):

    deleteEtatBudget = EtatBudget.objects.get(pk=pk)
    deleteEtatBudget.delete()

    return redirect('etat-budget')

def EtatBudgetsMeps(request):
    eBudgets = EtatBudget.objects.all()
    context = {
        'eBudgets': eBudgets
    }
    return render(request, 'home/documents/etat_budgets.html', context)



    # Nouveau

def addCategory(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
   
    return render(request, 'accounts/pages/documents/ajouter_category.html', {'form':form, 'categories': categories})

def editCategory(request, pk):

    editCat = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None,  instance=editCat)

        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm(instance=editCat)

    return render(request, 'accounts/pages/documents/ajouter_category.html', {'form': form})

def deleteCategory(request, pk):

    deleteCategory = Category.objects.get(pk=pk)
    deleteCategory.delete()
    return redirect('add_category')

def CategoryView(request, cats):
    category_posts = Budget.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'home/documents/categories.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts':category_posts})