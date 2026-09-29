from django.db import models

# Create your models here.
class Offre(models.Model):
    prix = models.DecimalField(max_digits=10,decimal_places=2)
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(max_length=20,choices=[
        ('p','proposee'),
        ('a','acceptee'),
        ('r','refusee')
        ('ret','retiree')
    ],default='proposee')
    date_proposition = models.DateTimeField(auto_now_add=True)
    expedition = models.ForeignKey(Expedition,on_delete=models.CASCADE,related_name='offres')
    vehicule = models.ForeignKey(Vehicule,on_delete=models.CASCADE,related_name='offres')
    transporteur = models.ForeignKey(utilisateur,on_delete=models.CASCADE,related_name='offres')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)