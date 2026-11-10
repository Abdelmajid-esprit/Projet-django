from django.db import models
from django.core.validators import MinValueValidator


class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, unique=True)

    type_vehicule = models.CharField(
        max_length=50,
        choices=[
            ('camion', 'Camion'),
            ('fourgon', 'Fourgon'),
            ('voiture', 'Voiture'),
        ]
    )

    capacite_kg = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                1,
                "La capacité du véhicule doit être supérieure à 0"
            )
        ]
    )

    disponible = models.BooleanField(default=True)

    entreprise = models.ForeignKey(
        'EntrepriseApp.Entreprise',
        on_delete=models.CASCADE,
        related_name='vehicules'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.immatriculation
