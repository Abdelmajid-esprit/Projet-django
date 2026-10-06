from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Expedition(models.Model):
    reference = models.CharField(max_length=20,unique=True)
    poid_kg = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(1,"Le poid de l'expedition doit être supérieur à 0")])
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

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'c':
            raise ValidationError("Une expédition doit être associée à une entreprise de type 'Chargeur'.")

    def _generate_reference(cls):
        annee=timezone.now().strftime('%Y')
        prefixe = f"EXP_{annee}_"
        dernier=cls.objects.filter(reference__startswith=prefixe).order_by('reference').last()
        compteur=int(dernier.reference[-5:]) + 1 if dernier else 1
        if compteur > 99999:
            raise ValidationError("Le compteur a dépassé la limite maximale de 99999.")
        return f"{prefixe}{compteur:05d}"
    
    def _generate_user_id(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"{annee}user"
        dernier = cls.objects.filter(user_id__startswith=prefixe).order_by('user_id').last()
        if dernier:
            dernier_id = dernier.user_id
            dernier_num = int(dernier_id[-2:])
            nouveau = dernier_num + 1
        else:
            nouveau = 1
        if nouveau > 99:
            raise ValidationError("Le compteur a dépassé la limite maximale de 99.")
        return f"{prefixe}{nouveau:02d}"

    def save (self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        self.full_clean()  # Valide les champs avant de sauvegarder
        super().save(*args, **kwargs)
