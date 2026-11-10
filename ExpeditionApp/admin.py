from django.contrib import admin
from OffreApp.models import Offre
from .models import Expedition


class OffreInline(admin.TabularInline):
    model = Offre
    extra = 0
    fk_name= 'expedition'
    show_change_link = True
    can_delete = False

class ExpeditionAdmin(admin.ModelAdmin):
    inlines = [OffreInline]
    list_display = ("reference", "poid_kg", "status", "entreprise", "created_at")
    list_filter = ("status",)
    search_fields = ("reference", "entreprise__raison_social")
    readonly_fields = ("reference", "created_at", "updated_at")
    fieldsets = (
        ("Informations de l'expédition", {
            "fields": ("reference", "poid_kg", "status")
        }),
        ("Entreprise associée", {
            "fields": ("entreprise",)
        }),
        ("Horodatage", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        })
    )
admin.site.register(Expedition, ExpeditionAdmin)
# Register your models here.
