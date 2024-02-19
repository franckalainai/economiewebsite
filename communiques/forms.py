from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *

class CommuniqueForm(forms.ModelForm):
    class Meta:
        model = Communique
        fields = ('titre', 'pdf',)
    
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Nom du document...'}),
                
            }