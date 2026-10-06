from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20,unique=True)
    capacite_kg = models.PositiveIntegerField(validators=[MinValueValidator(1,"La capacité du véhicule doit être supérieure à 0")])
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise',on_delete=models.CASCADE,related_name='vehicule')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
