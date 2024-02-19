from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# creating a form
class ZoomForm(forms.ModelForm):
    class Meta:
        model = Zoom
        fields = ['titre', 'slug', 'resume', 'description', 'image']
        #fields = '__all__'

        titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        resume = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
        description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
        image = forms.ImageField()
        #status = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
   

        labels = {

            'titre': 'Titre',
            'slug': 'slug',
            'resume': 'Resume',
            'description': 'description',
        }
        widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Titre...'}),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slugHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Url...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'resumeHere', 'aria-describedby': 'resumeHelp', 'placeholder': 'Resume...'}),
            'description': SummernoteWidget(),
        }