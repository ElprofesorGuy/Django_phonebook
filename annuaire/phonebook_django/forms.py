from django import forms
from .models import Contact

class newContactForm(forms.ModelForm):
    #name = forms.CharField(label = "Nom")
    #phoneNumber = forms.CharField(label = "Numero de téléphone")
    #categories
    class Meta:
        model = Contact
        fields = ['name', 'phoneNumber', 'categorie', 'city']
        labels = {'name': "Nom", "phoneNumber":"Numéro de téléphone"}