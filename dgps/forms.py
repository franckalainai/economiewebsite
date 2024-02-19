from django.forms import TextInput
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

choices = Category.objects.all().values_list('name','name') 
#name is from model field
choice_list = []

for item in choices:
    choice_list.append(item)

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = '__all__'
    
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Titre...'}),
            'resume': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Résumé...'}),
            'description': SummernoteWidget(),
                
            }
    
class CategoryForm(forms.ModelForm): 
    class Meta:
        model = Category
        fields = ('name',)

#for bootstrap
        widgets = {
            'name': forms.TextInput(
            	attrs={'class': 'form-control'}), 
        }