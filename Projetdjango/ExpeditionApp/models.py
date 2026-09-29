from django.db import models
from EntrepriseApp.models import Entreprise

# Create your models here.
class Expedition(models.Model):
    reference = models.CharField(max_length=20,unique=True)
    poid_kg = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=[
        ('p','publiee'),
        ('a','attribuee'),
        ('e','en cours'),
        ('l','livree'),
        ('an','annulee')
    ],default='publiee')
    entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE,related_name='expedition')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)