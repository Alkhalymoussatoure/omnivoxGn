from django.db import models

# Create your models here.

class Etablissement(models.Model):
    
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nom