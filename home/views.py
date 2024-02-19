from django.shortcuts import render, redirect
import directions
from faq.models import Faq
from meps_.models import *
from banniere.models import *
from actualites.models import *
from actualites.views import *
from banniere.views import *
from emploi.views import *
from faq.views import *
from directions.views import *
from directions.models import *
from zoom.views import *
from ministere.models import Biographie
from . models import *
from zoom.models import Zoom
from . models import *
from .forms import *

import os

# Create your views here.
def home(request):
    ministere = Ministere.objects.first()
    bios = Biographie.objects.first()
    bannieres = Banner.objects.all()
    photos = PhotoMinistre.objects.all()
    actualites = Actualite.objects.all()[:3]
    actuhome = Actualite.objects.all()[:3]
    zooms = Zoom.objects.all()[:3]
    emplois = Emploi.objects.first()

    page = request.GET.get('page', 1)

    paginator = Paginator(actualites, 1)
    try:
        actualites = paginator.page(page)
    except PageNotAnInteger:
        actualites = paginator.page(1)
    except EmptyPage:
        actualites = paginator.page(paginator.num_pages)

    context = {
        'ministere': ministere, 
        'bannieres': bannieres,
        'photos': photos,
        'actualites': actualites,
        'emplois': emplois,
        'actuhome': actuhome,
        'bios': bios,
        'zooms': zooms
        }

    return render(request, 'home/index.html', context)
    

def orga(request):
    return render(request, 'home/meps/organigramme.html')
    
def cmu2(request):
    filepath = os.path.join('static', 'home/Organigramme/sites-enrolements.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    

def sousTutelles(request):
    return render(request, 'home/meps/sous_tutelles.html')

def ecolesSpeciales(request):
    return render(request, 'home/meps/ecoles.html')


def decretOrga(request):
    return render(request, 'home/meps/decret.html')

def get_faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'home/faq.html', context)


def equipe(request):
    return render(request, 'home/equipe.html')

