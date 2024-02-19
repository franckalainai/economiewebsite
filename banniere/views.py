from multiprocessing import context
from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.
def add_banner(request):
    banners = Banner.objects.all()

    if request.method == 'POST':
        form = BannerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-banner')
    else:
        form = BannerForm()
   
    return render(request, 'accounts/pages/banner/banner.html', {'form':form,'banners': banners})

def editbanner(request, pk):

    editBan = Banner.objects.get(pk=pk)

    form = BannerForm(request.POST, request.FILES, instance=editBan)

    if form.is_valid():
        form.save()
        return redirect('add-banner')

    return render(request, 'accounts/pages/banner/edit-banner.html', {'form': form})


def add_photo(request):
    photos = PhotoMinistre.objects.all()

    if request.method == 'POST':
        form = PhotoMinistreForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-photo')
    else:
        form = PhotoMinistreForm()
   
    return render(request, 'accounts/pages/banner/add_photo.html', {'form':form,'photos': photos})


def editPhoto(request, pk):

    editPhoto = PhotoMinistre.objects.get(pk=pk)
    if request.method == 'POST':
        form = PhotoMinistreForm(request.POST or None, request.FILES,  instance=editPhoto)

        if form.is_valid():
            form.save()
            return redirect('add-photo')
    else:
        form = PhotoMinistreForm(instance=editPhoto)

    return render(request, 'accounts/pages/banner/add_photo.html', {'form': form})


def deletePhoto(request, pk):

    deletePhoto = PhotoMinistre.objects.get(pk=pk)
    deletePhoto.delete()

    return redirect('add-photo')