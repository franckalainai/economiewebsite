from random import choices
from django.forms import ModelForm, TextInput, Textarea, ChoiceField
from .models import *
from actualites.models import *

class FaqForm(ModelForm):
    class Meta:
        model = Faq
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'question': 'question',
            'slug': 'slug',
            'reponse': 'reponse',
        }
        widgets = {
            'question': TextInput(attrs={'class': 'form-control', 'id': 'nomHere', 'aria-describedby': 'nomHelp', 'placeholder': 'nom...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'slug...'}),
            'reponse': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
        }