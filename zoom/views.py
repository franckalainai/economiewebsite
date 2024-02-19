from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import ZoomForm
from django.contrib import messages
import os
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

@login_required(login_url='login')
def zoom(request):
    
    zooms = Zoom.objects.all()
    if request.method == 'POST':
        form = ZoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            return redirect('zoom')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = ZoomForm()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(zooms, 4)
    try:
        zooms = paginator.page(page)
    except PageNotAnInteger:
        zooms = paginator.page(1)
    except EmptyPage:
        zooms = paginator.page(paginator.num_pages)

    return render(request, 'accounts/pages/zooms/zooms.html', {'form': form, 'zooms': zooms})

def zooms(request):
    
    zooms = Zoom.objects.all()
    context = {
        'zooms': zooms
    }
    return render(request, 'home/zooms.html', context)

def editzoom(request, pk):
    editActu = Zoom.objects.get(pk=pk)
    if request.method == 'POST':
        form = ZoomForm(request.POST or None, request.FILES,  instance=editActu)

        if form.is_valid():
            form.save()
            return redirect('zoom')
    else:
        form = ZoomForm(instance=editActu)

    return render(request, 'accounts/pages/zooms/zooms.html', {'form': form})

def deletezoom(request, pk):

    deleteActu = Zoom.objects.get(pk=pk)
    deleteActu.delete()

    return redirect('zoom')

def detail_zoom(request, slug):
    context = {}
    try:
        blog_obj = Zoom.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_zoom.html', context)