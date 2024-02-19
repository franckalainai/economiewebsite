from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import ActualiteForm
from django.contrib import messages
import os
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

@login_required(login_url='login')
def actualites(request):
    
    actualites = Actualite.objects.all()
    if request.method == 'POST':
        form = ActualiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            return redirect('actualites')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = ActualiteForm()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(actualites, 4)
    try:
        actualites = paginator.page(page)
    except PageNotAnInteger:
        actualites = paginator.page(1)
    except EmptyPage:
        actualites = paginator.page(paginator.num_pages)

    return render(request, 'accounts/pages/actualites/actualites.html', {'form': form, 'actualites': actualites})

def actu(request):
    
    actualites = Actualite.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(actualites, 4)
    try:
        actualites = paginator.page(page)
    except PageNotAnInteger:
        actualites = paginator.page(1)
    except EmptyPage:
        actualites = paginator.page(paginator.num_pages)
    context = {
        'actualites': actualites
    }
    return render(request, 'home/actualites.html', context)

@login_required(login_url='login')
def editactualites(request, pk):
    editActu = Actualite.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActualiteForm(request.POST or None, request.FILES,  instance=editActu)

        if form.is_valid():
            form.save()
            return redirect('actualites')
    else:
        form = ActualiteForm(instance=editActu)

    return render(request, 'accounts/pages/actualites/actualites.html', {'form': form})

@login_required(login_url='login')
def deleteActualites(request, pk):

    deleteActu = Actualite.objects.get(pk=pk)
    deleteActu.delete()

    return redirect('actualites')

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = Actualite.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail.html', context)