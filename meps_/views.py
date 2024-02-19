from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from actualites.models import *
from .forms import *
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def ministere(request):
    
    #ministere = Ministere.objects.last()
    ministeres = Ministere.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = MinistereForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('ministere')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = MinistereForm()
    return render(request, 'accounts/pages/ministere/ministere.html', {'form': form, 'ministeres': ministeres})


def editMinistere(request, pk):

    editMins = Ministere.objects.get(pk=pk)
    if request.method == 'POST':
        form = MinistereForm(request.POST or None, request.FILES,  instance=editMins)

        if form.is_valid():
            form.save()
            return redirect('ministere')
    else:
        form = MinistereForm(instance=editMins)

    return render(request, 'accounts/pages/ministere/ministere.html', {'form': form})

def deleteMinistere(request, pk):

    deleteMinistere = Ministere.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('ministere')

def detailMinistere(request, slug):
    context = {}
    try:
        blog_obj = Ministere.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_ministere.html', context)
    
def directeurs(request):
    return render(request, 'home/meps/directeurs.html')