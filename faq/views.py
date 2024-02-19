from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.contrib import messages

# Create your views here.



def faq(request):
    
    #ministere = Ministere.objects.last()
    faqs = Faq.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('faq')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = FaqForm()
    return render(request, 'accounts/pages/faq/faq.html', {'form': form, 'faqs': faqs})


def editFaq(request, pk):

    editMins = Faq.objects.get(pk=pk)
    if request.method == 'POST':
        form = FaqForm(request.POST or None, request.FILES,  instance=editMins)

        if form.is_valid():
            form.save()
            return redirect('faq')
    else:
        form = FaqForm(instance=editMins)

    return render(request, 'accounts/pages/faq/faq.html', {'form': form})

def deleteFaq(request, pk):

    deleteMinistere = Faq.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('faq')

def detailFaq(request, slug):
    context = {}
    try:
        blog_obj = Faq.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_faq.html', context)