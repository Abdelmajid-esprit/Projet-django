from django.db import models

# Create your models here.
class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20,unique=True)
    capacite_kg = models.PositiveIntegerField()
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise',on_delete=models.CASCADE,related_name='vehicule')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
