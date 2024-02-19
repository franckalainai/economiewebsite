from django.shortcuts import render, redirect

# Create your views here.
from . models import *
from .forms import *

# Create your views here.

# Fonctions de gestion des budgets vitrine
def communiques(request):
    communiques = Communique.objects.all()
    return render(request, 'home/communiques/communiques.html', {'communiques': communiques})


def creerCommunique(request):
    communiques = Communique.objects.all()

    if request.method == 'POST':
        form = CommuniqueForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('communique')
    else:
        form = CommuniqueForm()
   
    return render(request, 'accounts/pages/communiques/communiques.html', {'form':form,'communiques': communiques})


def editCommunique(request, pk):

    editCom = Communique.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommuniqueForm(request.POST or None, request.FILES,  instance=editCom)

        if form.is_valid():
            form.save()
            return redirect('communique')
    else:
        form = CommuniqueForm(instance=editCom)

    return render(request, 'accounts/pages/communiques/communiques.html', {'form': form})

def deleteCommunique(request, pk):

    deleteCommunique = Communique.objects.get(pk=pk)
    deleteCommunique.delete()

    return redirect('communique')