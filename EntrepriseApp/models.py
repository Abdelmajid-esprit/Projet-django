from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone


#Validators
def validate_email(value):
    if not value:
        raise ValidationError("L'adresse email ne peut pas être Obligatoire")
    if not value.endswith('@gmail.com'):
        raise ValidationError("Le domaine accepté est @gmail.com")

matricule_fiscale_validator = RegexValidator(    
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="Le format du matricule fiscale est invalide."
)
telephone_validator = RegexValidator(
    regex=r'^\+?[0-9]{8,15}$',
    message="Le téléphone doit contenir entre 8 et 15 chiffres.",
)

# Create your models here.
class utilisateur(AbstractUser):
    user_id = models.CharField(primary_key=True,max_length=8)
    email = models.EmailField(unique=True,validators=[validate_email])
    telephone = models.CharField(max_length=15, blank=True, null=True, validators=[telephone_validator])
    role = models.CharField(max_length=20,choices=[
        ('admin','Admin'),
        ('c','Chargeur'),
        ('t','Transporteur')],default='c')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_user_id()
        self.full_clean()
        super().save(*args, **kwargs)

    @classmethod
    def generate_user_id(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"{annee}USR"
        dernier = (
            cls.objects
            .filter(user_id__startswith=prefixe)
            .order_by('-user_id')
            .first()
        )
        compteur = int(dernier.user_id[-2:]) + 1 if dernier else 1
        if compteur > 99:
            raise ValidationError("Limite de 100 utilisateurs atteinte pour cette année.")
        return f"{prefixe}{compteur:02d}"

class Entreprise(models.Model):
    raison_social = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3, "La raison sociale doit contenir au moins 3 caractères.")],
    )
    matricule_fiscale = models.CharField(
        max_length=17,
        unique=True,
        validators=[matricule_fiscale_validator],
    )
    adresse = models.TextField(validators=[
        MinLengthValidator(20,"L'adresse ne peut pas être inférieure à 20 caractères"),MaxLengthValidator(400,"L'adresse ne peut pas dépasser les 400 caractères")
    ])
    type_entreprise = models.CharField(max_length=100,choices=[
        ('c','Chargeur'),
        ('t','Transporteur')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(utilisateur,on_delete=models.CASCADE,related_name='entreprise') 

    def clean(self):
        super().clean()
        if self.gerant_id and self.gerant.role not in ("admin", "c", "t"):
            raise ValidationError({"gerant": "Le gérant sélectionné possède un rôle invalide."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

