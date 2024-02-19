from django.forms import ModelForm, TextInput, Textarea, ChoiceField, ImageField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import *

class BannerForm(ModelForm):
    class Meta:
        model = Banner
        fields = ('nom', 'image', 'resume')

        labels = {

            'nom': 'nom',
            'image': 'image',
            'resume': 'Resume',
            }
        
        widgets = {
            'nom': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Nom...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Résumé...'}),
            }


class PhotoMinistreForm(ModelForm):
    class Meta:
        model = PhotoMinistre
        fields = ('nom', 'image')

        labels = {

            'nom': 'nom',
            'image': 'image'
            }
        
        widgets = {
            'nom': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Nom...'}),
            }