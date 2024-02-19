from random import choices
from django.forms import ModelForm, TextInput, Textarea, ChoiceField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import *
from actualites.models import *

class MissionForm(ModelForm):
    class Meta:
        model = Mission
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
            'slug': 'slug',
            'resume': 'Resume',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }


class CabinetForm(ModelForm):
    class Meta:
        model = Cabinet
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
            'slug': 'slug',
            'resume': 'Resume',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }

class OrganigrammeForm(ModelForm):
    class Meta:
        model = Organigramme
        #fields = ['content', 'added_time']
        fields = ('titre', 'pdf',)

        labels = {

            'titre': 'titre',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
        }

class TutelForm(ModelForm):
    class Meta:
        model = Tutel
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
            'slug': 'slug',
            'contact': 'contact',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'contact': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }

class EcoleForm(ModelForm):
    class Meta:
        model = Ecole
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
            'slug': 'slug',
            'contact': 'contact',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'contact': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }

class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
        }


class BiographieForm(ModelForm):
    class Meta:
        model = Biographie
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
            'slug': 'slug',
            'resume': 'Resume',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }
        
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'titre',
            'slug': 'slug',
            'resume': 'Resume',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }