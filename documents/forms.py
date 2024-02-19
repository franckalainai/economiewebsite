from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *

choices = Category.objects.all().values_list('name','name') 
#name is from model field
choice_list = []

for item in choices:
    choice_list.append(item)

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('titre', 'category', 'pdf',)
    
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Nom du document...'}),
                
            }

class EtatBudgetForm(forms.ModelForm):
    class Meta:
        model = EtatBudget
        fields = ('titre', 'pdf',)
    
    widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Titre...'}),
        }

class PlanPassationForm(forms.ModelForm):
    class Meta:
        model = PlanPassation
        fields = ('titre', 'pdf',)
    
    widgets = {
            'titre': TextInput(attrs={'class': 'form-control', 'id': 'titreHere', 'aria-describedby': 'titreHelp', 'placeholder': 'Titre...'}),
        }

# Nouveau
class CategoryForm(forms.ModelForm): 
    class Meta:
        model = Category
        fields = ('name',)

#for bootstrap
        widgets = {
            'name': forms.TextInput(
            	attrs={'class': 'form-control'}), 
        }