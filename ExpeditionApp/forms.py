from django import forms
from .models import Expedition




class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields ="__all__"
        exclude = ["id","reference", "created_at", "updated_at"]
        widgets = {
            "poid_kg": forms.NumberInput(attrs={
                "min": "1",
                "step": "0.01",
                "placeholder": "Exemple : 1250",
            }),
        }
        labels = {
            "poid_kg": "Poids (kg)",
            "status": "Statut",
            "entreprise": "Entreprise chargeur",
        }