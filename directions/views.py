from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def homedirection(request):
    directions = Direction.objects.all()
    context = {
        'directions': directions
    }
    return render(request, 'home/direction.html', context)



def detaildirection(request, slug):
    context = {}
    try:
        blog_obj = Direction.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_direction.html', context)

def directionDashboard(request):
    
    return render(request, 'accounts/pages/direction/dashboard.html')


def direction(request):
    
    #ministere = Ministere.objects.last()
    directions = Direction.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = DirectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('direction')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = DirectionForm()
    return render(request, 'accounts/pages/direction/direction.html', {'form': form, 'directions': directions})


def editdirection(request, pk):

    editMins = Direction.objects.get(pk=pk)
    if request.method == 'POST':
        form = DirectionForm(request.POST or None, request.FILES,  instance=editMins)

        if form.is_valid():
            form.save()
            return redirect('direction')
    else:
        form = DirectionForm(instance=editMins)

    return render(request, 'accounts/pages/direction/direction.html', {'form': form})

def deletedirection(request, pk):

    deleteMinistere = Direction.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('direction')

def detaildirection(request, slug):
    try:
        blog_obj = Direction.objects.filter(slug=slug).first()
        categorys = {category: Direction.objects.filter(category = category) for category in Category.objects.all()}

        context = {'blog_obj': blog_obj, 'categorys': categorys}
    except Exception as e:
        print(e)
    return render(request, 'home/detail_direction.html', context)


def addCategory(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = DirectionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-direction-category')
    else:
        form = DirectionForm()
   
    return render(request, 'accounts/pages/direction/ajouter_category.html', {'form':form, 'categories': categories})

def editCategory(request, pk):

    editCat = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = DirectionForm(request.POST or None,  instance=editCat)

        if form.is_valid():
            form.save()
            return redirect('add-direction-category')
    else:
        form = DirectionForm(instance=editCat)

    return render(request, 'accounts/pages/direction/ajouter_category.html', {'form': form})

def deleteCategory(request, pk):

    deleteCategory = Category.objects.get(pk=pk)
    deleteCategory.delete()
    return redirect('add-direction-category')

def CategoryView(request, cats):
    category_posts = Category.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'home/direction.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts':category_posts})

