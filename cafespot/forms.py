from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilizator, Recenzie

class UtilizatorRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilizator
        fields = ('username', 'email')

class RecenzieForm(forms.ModelForm):
    class Meta:
        model = Recenzie
        fields = ('rating', 'comentariu')
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comentariu': forms.Textarea(attrs={'rows': 3}),
        }