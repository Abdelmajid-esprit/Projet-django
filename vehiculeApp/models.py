from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

immatriculation_validator = RegexValidator(
    regex=r'^\d{1,4}\s?[A-Z]{1,3}\s?\d{1,4}$',
    message="Format d'immatriculation invalide. Exemple : 1234 TUN 567.",
)

# Create your models here.
class Vehicule(models.Model):
    immatriculation = models.CharField(
        max_length=20,
        unique=True,
        validators=[immatriculation_validator],
    )
    capacite_kg = models.PositiveIntegerField(validators=[MinValueValidator(1,"La capacité du véhicule doit être supérieure à 0")])
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise',on_delete=models.CASCADE,related_name='vehicule')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != "t":
            raise ValidationError({"entreprise": "Un véhicule doit appartenir à une entreprise Transporteur."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
