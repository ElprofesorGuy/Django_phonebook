from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 64, unique = True, verbose_name = "Nom")
    phoneNumber = models.IntegerField(unique = True, verbose_name = "Numéro téléphonique")
    categorie = models.CharField();
    city = models.CharField(verbose_name = "Ville de résidence")
    
