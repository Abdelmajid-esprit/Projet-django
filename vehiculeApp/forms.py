from django import forms
from .models import Vehicule


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        exclude = ("created_at", "updated_at")
        widgets = {
            "immatriculation": forms.TextInput(attrs={
                "placeholder": "Ex. 1234 TUN 567",
            }),
            "capacite_kg": forms.NumberInput(attrs={
                "min": "1",
                "step": "1",
            }),
        }
