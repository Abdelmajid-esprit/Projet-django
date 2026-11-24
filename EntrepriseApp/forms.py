from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import utilisateur, Entreprise


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = utilisateur
        fields = ("username", "email", "telephone", "role")
        labels = {
            "username": "Nom d'utilisateur",
            "email": "Adresse e-mail",
            "telephone": "Téléphone",
            "role": "Type de compte",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Votre nom d'utilisateur"
        self.fields["email"].widget.attrs["placeholder"] = "exemple@gmail.com"
        self.fields["telephone"].widget.attrs["placeholder"] = "+216 XX XXX XXX"

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.user_id:
            user.user_id = utilisateur.generate_user_id()
        if commit:
            user.save()
        return user


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        exclude = ("created_at", "updated_at")
        widgets = {
            "raison_social": forms.TextInput(attrs={"placeholder": "Raison sociale"}),
            "matricule_fiscale": forms.TextInput(attrs={"placeholder": "Ex. 1234567/A/B/000"}),
            "adresse": forms.Textarea(attrs={"rows": 3, "placeholder": "Adresse complète"}),
        }
