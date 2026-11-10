from django.contrib import admin
from .models import Vehicule

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ("immatriculation", "capacite_kg", "entreprise")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Identification", {
            "fields": ("immatriculation", "capacite_kg")
        }),
        ("Rattachement", {
            "fields": ("entreprise",)
        }),
        ("Horodatage", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
