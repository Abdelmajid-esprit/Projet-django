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

# Create your models here.
class utilisateur(AbstractUser):
    user_id = models.CharField(primary_key=True,max_length=8)
    email = models.EmailField(unique=True,validators=[validate_email])
    telephone = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=20,choices=[
        ('admin','Admin'),
        ('c','Chargeur'),
        ('t','Transporteur')],default='c')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def save(self, *args, **kwargs):
    if not self.user_id:
        self.user_id = self.generate_user_id()
    #full_clean()  # Validate the model fields before saving
    self.full_clean()  # Validate the model fields before saving
    super().save(*args, **kwargs) 

@classmethod
def generate_user_id(cls):
    annee = timezone.now().strftime('%y')  
    prefixe = f"{annee}USR"
    dernier=(
        cls.objects
        .filter(user_id__startswith=prefixe)
        .order_by('-user_id')
        .first()
    )
    compteur = int(dernier.user_id[-2:]) + 1 if dernier else 0
    if compteur > 99:
        raise ValueError(f"Limite de 100 utilisateurs atteinte pour l'année 20{annee}."
        )
    return f"{prefixe}{compteur:02d}"

class Entreprise(models.Model):
    raison_social= models.CharField(max_length=200,blank=False,null=False)
    matricule_fiscale = models.CharField(max_length=17,unique=True)
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

