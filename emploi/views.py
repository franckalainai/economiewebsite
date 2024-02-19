from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def homeDge(request):
    
    return render(request, 'home/dge.html')

def dgeDashboard(request):
    
    return render(request, 'accounts/pages/dge/dashboard.html')


def dge(request):
    
    #ministere = Ministere.objects.last()
    emplois = Emploi.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = EmploiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('dge')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = EmploiForm()
    return render(request, 'accounts/pages/dge/dge.html', {'form': form, 'emplois': emplois})


def editDge(request, pk):

    editMins = Emploi.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmploiForm(request.POST or None, request.FILES,  instance=editMins)

        if form.is_valid():
            form.save()
            return redirect('dge')
    else:
        form = EmploiForm(instance=editMins)

    return render(request, 'accounts/pages/dge/dge.html', {'form': form})

def deleteDge(request, pk):

    deleteMinistere = Emploi.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('dge')

def detailDge(request, slug):
    try:
        blog_obj = Emploi.objects.filter(slug=slug).first()
        categorys = {category: Emploi.objects.filter(category = category) for category in Category.objects.all()}

        context = {'blog_obj': blog_obj, 'categorys': categorys}
    except Exception as e:
        print(e)
    return render(request, 'home/detail_dge.html', context)


def addCategory(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-dge-category')
    else:
        form = CategoryForm()
   
    return render(request, 'accounts/pages/dge/ajouter_category.html', {'form':form, 'categories': categories})

def editCategory(request, pk):

    editCat = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None,  instance=editCat)

        if form.is_valid():
            form.save()
            return redirect('add-dge-category')
    else:
        form = CategoryForm(instance=editCat)

    return render(request, 'accounts/pages/dge/ajouter_category.html', {'form': form})

def deleteCategory(request, pk):

    deleteCategory = Category.objects.get(pk=pk)
    deleteCategory.delete()
    return redirect('add-dge-category')

def CategoryView(request, cats):
    category_posts = Category.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'home/dge.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts':category_posts})