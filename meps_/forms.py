from random import choices
from django.forms import ModelForm, TextInput, Textarea, ChoiceField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import *
from actualites.models import *

# creating a form
class MinistereForm(ModelForm):
    class Meta:
        model = Ministere
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'titre': 'Titre',
            'slug': 'slug',
            'resume': 'Resume',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Titre...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }

