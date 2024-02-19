from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.contrib import messages

# Create your views here.


def mission(request):
    
    #ministere = Ministere.objects.last()
    missions = Mission.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('mission')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = MissionForm()
    return render(request, 'accounts/pages/ministere/mission.html', {'form': form, 'missions': missions})


def editMission(request, pk):

    editMins = Mission.objects.get(pk=pk)
    if request.method == 'POST':
        form = MissionForm(request.POST or None, request.FILES,  instance=editMins)

        if form.is_valid():
            form.save()
            return redirect('mission')
    else:
        form = MissionForm(instance=editMins)

    return render(request, 'accounts/pages/ministere/mission.html', {'form': form})

def deleteMission(request, pk):

    deleteMinistere = Mission.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('mission')

def detailMission(request, slug):
    context = {}
    try:
        blog_obj = Mission.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_mission.html', context)


# Cabinet
def cabinet(request):
    
    #ministere = Ministere.objects.last()
    cabinets = Cabinet.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = CabinetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('cabinet')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = CabinetForm()
    return render(request, 'accounts/pages/ministere/cabinet.html', {'form': form, 'cabinets': cabinets})


def editCabinet(request, pk):

    editCab = Cabinet.objects.get(pk=pk)
    if request.method == 'POST':
        form = CabinetForm(request.POST or None, request.FILES,  instance=editCab)

        if form.is_valid():
            form.save()
            return redirect('cabinet')
    else:
        form = CabinetForm(instance=editCab)

    return render(request, 'accounts/pages/ministere/cabinet.html', {'form': form})

def deleteCabinet(request, pk):

    deleteMinistere = Cabinet.objects.get(pk=pk)
    deleteMinistere.delete()

    return redirect('cabinet')

def detailCabinet(request, slug):
    context = {}
    try:
        blog_obj = Cabinet.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_cabinet.html', context)


# organigramme
def organigramme(request):
    
    #ministere = Ministere.objects.last()
    organigrammes = Organigramme.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = OrganigrammeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('organigramme')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = OrganigrammeForm()
    return render(request, 'accounts/pages/ministere/organigramme.html', {'form': form, 'organigrammes': organigrammes})


def editOrganigramme(request, pk):

    editOrg = Organigramme.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrganigrammeForm(request.POST or None, request.FILES,  instance=editOrg)

        if form.is_valid():
            form.save()
            return redirect('organigramme')
    else:
        form = OrganigrammeForm(instance=editOrg)

    return render(request, 'accounts/pages/ministere/organigramme.html', {'form': form})

def deleteOrganigramme(request, pk):

    deleteOrganigramme = Organigramme.objects.get(pk=pk)
    deleteOrganigramme.delete()

    return redirect('cabinet')

def detailOrganigramme(request, slug):
    context = {}
    try:
        blog_obj = Organigramme.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_organigramme.html', context)


# tutelle
def tutel(request):
    
    #ministere = Ministere.objects.last()
    tutels = Tutel.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = TutelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('tutel')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = TutelForm()
    return render(request, 'accounts/pages/ministere/tutel.html', {'form': form, 'tutels': tutels})


def editTutel(request, pk):

    editTutel = Tutel.objects.get(pk=pk)
    if request.method == 'POST':
        form = TutelForm(request.POST or None, request.FILES,  instance=editTutel)

        if form.is_valid():
            form.save()
            return redirect('tutel')
    else:
        form = TutelForm(instance=editTutel)

    return render(request, 'accounts/pages/ministere/tutel.html', {'form': form})

def deleteTutel(request, pk):

    deleteTut = Tutel.objects.get(pk=pk)
    deleteTut.delete()

    return redirect('tutel')

def detailTutel(request, slug):
    context = {}
    try:
        blog_obj = Tutel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_tutel.html', context)


# ecole
def ecole(request):
    
    #ministere = Ministere.objects.last()
    ecoles = Ecole.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = EcoleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('ecole')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = EcoleForm()
    return render(request, 'accounts/pages/ministere/ecole.html', {'form': form, 'ecoles': ecoles})


def editEcole(request, pk):

    editEco = Ecole.objects.get(pk=pk)
    if request.method == 'POST':
        form = EcoleForm(request.POST or None, request.FILES,  instance=editEco)

        if form.is_valid():
            form.save()
            return redirect('ecole')
    else:
        form = EcoleForm(instance=editEco)

    return render(request, 'accounts/pages/ministere/ecole.html', {'form': form})

def deleteEcole(request, pk):

    deleteEco = Ecole.objects.get(pk=pk)
    deleteEco.delete()

    return redirect('ecole')

def detailEcole(request, slug):
    context = {}
    try:
        blog_obj = Ecole.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_ecole.html', context)



def organisation(request):
    
    #ministere = Ministere.objects.last()
    organisations = Organisation.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = OrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('organisation')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = OrganisationForm()
    return render(request, 'accounts/pages/ministere/organisation.html', {'form': form, 'organisations': organisations})


def editOrganisation(request, pk):

    editOrga = Organisation.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrganisationForm(request.POST or None, request.FILES,  instance=editOrga)

        if form.is_valid():
            form.save()
            return redirect('organisation')
    else:
        form = OrganigrammeForm(instance=editOrga)

    return render(request, 'accounts/pages/ministere/organisation.html', {'form': form})

def deleteOrganisation(request, pk):

    deleteOrganisation = Organisation.objects.get(pk=pk)
    deleteOrganisation.delete()

    return redirect('organisation')

def detailOrganisation(request, slug):
    context = {}
    try:
        blog_obj = Organisation.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_organisation.html', context)



# Biographie
def biographie(request):
    
    #ministere = Ministere.objects.last()
    biographies = Biographie.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = BiographieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('biographie')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = BiographieForm()
    return render(request, 'accounts/pages/ministere/biographie.html', {'form': form, 'biographies': biographies})


def editBiographie(request, pk):

    eitBiographie = Biographie.objects.get(pk=pk)
    if request.method == 'POST':
        form = BiographieForm(request.POST or None, request.FILES,  instance=eitBiographie)

        if form.is_valid():
            form.save()
            return redirect('biographie')
    else:
        form = BiographieForm(instance=eitBiographie)

    return render(request, 'accounts/pages/ministere/biographie.html', {'form': form})

def deleteBiographie(request, pk):

    deleteBiographie = Biographie.objects.get(pk=pk)
    deleteBiographie.delete()

    return redirect('biographie')

def detailBiographie(request, slug):
    context = {}
    try:
        blog_obj = Biographie.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_biographie.html', context)
    
# produit
def produit(request):
    
    #ministere = Ministere.objects.last()
    produits = Produit.objects.all()
    #ministere = Ministere.objects.filter(status=1).order_by('-created_at')
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article crée avec succès.')
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #context = {'form': form, 'img_obj': img_obj, 'sent': True}
            #return render(request, 'accounts/pages/ministere/ministere.html', context)
            return redirect('produit')
        else:
            messages.error(request, 'Un problème est survenu, veuillez réessayer svp.')
            messages.error(request, form.errors)
    else:
        form = ProduitForm()
    return render(request, 'accounts/pages/ministere/produit.html', {'form': form, 'produits': produits})


def editProduit(request, pk):

    eitproduit = Produit.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST or None, request.FILES,  instance=eitproduit)

        if form.is_valid():
            form.save()
            return redirect('produit')
    else:
        form = ProduitForm(instance=eitproduit)

    return render(request, 'accounts/pages/ministere/produit.html', {'form': form})

def deleteProduit(request, pk):

    deleteproduit = Produit.objects.get(pk=pk)
    deleteproduit.delete()

    return redirect('produit')

def detailProduit(request, slug):
    context = {}
    try:
        blog_obj = Produit.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'home/detail_produit.html', context)


def centrecmu(request):
    return render(request, 'home/produits/centre.html')

def reseaux(request):
    return render(request, 'home/produits/reseaux.html')

def medicaments(request):
    return render(request, 'home/produits/medicaments.html')