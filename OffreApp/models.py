from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Offre(models.Model):
    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1, "Le prix doit être supérieur à 0.")],
    )
    delai_jours = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, "Le délai doit être d'au moins 1 jour."),
            MaxValueValidator(365, "Le délai ne peut pas dépasser 365 jours."),
        ],
    )
    statut = models.CharField(max_length=20,choices=[
        ('p','proposee'),
        ('a','acceptee'),
        ('r','refusee'),
        ('ret','retiree')
    ],default='p')
    date_proposition = models.DateTimeField(auto_now_add=True)
    expedition = models.ForeignKey('ExpeditionApp.Expedition',on_delete=models.CASCADE,related_name='offre')
    vehicule = models.ForeignKey('vehiculeApp.Vehicule',on_delete=models.CASCADE,related_name='offre')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise',on_delete=models.CASCADE,related_name='offre')

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != "t":
            raise ValidationError({"entreprise": "Une offre doit être créée par une entreprise Transporteur."})
        if self.vehicule_id and self.entreprise_id:
            if self.vehicule.entreprise_id != self.entreprise_id:
                raise ValidationError({"vehicule": "Le véhicule doit appartenir à la même entreprise que l'offre."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)