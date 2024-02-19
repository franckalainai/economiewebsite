from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

class AuthorSignUpForm(UserCreationForm):
    username = forms.CharField(required=True, label="Nom d'utilisateur")
    first_name = forms.CharField(required=True, label='Nom')
    last_name = forms.CharField(required=True, label='Prénom')
    email = forms.CharField(required=True, label='Email')
    password1 = forms.CharField(label='Mot de passe',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(label='Confirmez le mot de passe',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_author = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Author.objects.create(user=user)
        customer.save()
        return user