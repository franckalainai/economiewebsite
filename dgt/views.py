from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def homeDgt(request):
    
    return render(request, 'home/dgt.html')

def dgtDashboard(request):
    
    return render(request, 'accounts/pages/dgt/dashboard.html')


def dgt(request):
    
    #ministere = Ministere.objects.last()
    travaux = Travail.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = TravailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('dgt')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = TravailForm()
    return render(request, 'accounts/pages/dge/dge.html', {'form': form, 'travaux': travaux})


def editDgt(request, pk):

    editMins = Travail.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravailForm(request.POST or None, request.FILES,  instance=editMins)

        if form.is_valid():
            form.save()
            return redirect('dgt')
    else:
        form = TravailForm(instance=editMins)

    return render(request, 'accounts/pages/dgt/dgt.html', {'form': form})

def deleteDgt(request, pk):

    deleteMinistere = Travail.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('dgt')

def detailDgt(request, slug):
    try:
        blog_obj = Travail.objects.filter(slug=slug).first()
        categorys = {category: Travail.objects.filter(category = category) for category in Category.objects.all()}

        context = {'blog_obj': blog_obj, 'categorys': categorys}
    except Exception as e:
        print(e)
    return render(request, 'home/detail_dgt.html', context)


def addCategory(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-dgt-category')
    else:
        form = CategoryForm()
   
    return render(request, 'accounts/pages/dgt/ajouter_category.html', {'form':form, 'categories': categories})

def editCategory(request, pk):

    editCat = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None,  instance=editCat)

        if form.is_valid():
            form.save()
            return redirect('add-dgt-category')
    else:
        form = CategoryForm(instance=editCat)

    return render(request, 'accounts/pages/dgt/ajouter_category.html', {'form': form})

def deleteCategory(request, pk):

    deleteCategory = Category.objects.get(pk=pk)
    deleteCategory.delete()
    return redirect('add-dgt-category')

def CategoryView(request, cats):
    category_posts = Category.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'home/dgt.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts':category_posts})