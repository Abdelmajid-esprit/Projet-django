from django import forms
from .models import Offre


class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        exclude = ("created_at", "updated_at", "date_proposition")
        widgets = {
            "prix": forms.NumberInput(attrs={"min": "1", "step": "0.01"}),
            "delai_jours": forms.NumberInput(attrs={"min": "1", "max": "365", "step": "1"}),
        }
