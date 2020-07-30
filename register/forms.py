from django import forms

from django.contrib.auth.forms import UserCreationForm

from register.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    error_css_class = 'alert alert-primary'
    required_css_class = 'required'

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Nom d\'utilisateur'}),
        label='Nom d\'utilisateur')
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Adresse mail'}),
        label='E-mail ', required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Mot de passe'}),
        label='Votre mot de passe ')
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Confirmer mot de passe'}),
        label='Comfirmez vôtre mot de passe ')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
