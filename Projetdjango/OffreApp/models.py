from django.db import models


# Create your models here.
class Offre(models.Model):
    prix = models.DecimalField(max_digits=10,decimal_places=2)
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(max_length=20,choices=[
        ('p','proposee'),
        ('a','acceptee'),
        ('r','refusee'),
        ('ret','retiree')
    ],default='proposee')
    date_proposition = models.DateTimeField(auto_now_add=True)
    expedition = models.ForeignKey('ExpeditionApp.Expedition',on_delete=models.CASCADE,related_name='offre')
    vehicule = models.ForeignKey('vehiculeApp.Vehicule',on_delete=models.CASCADE,related_name='offre')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise',on_delete=models.CASCADE,related_name='offre')