from django.contrib import admin
from .models import utilisateur,Entreprise
from vehiculeApp.models import Vehicule
from django.contrib.auth.admin import UserAdmin



admin.site.site_header = "TransConnect - Administration"
admin.site.site_title = "TransConect"
admin.site.index_title = "Tableau de bord"
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_editable = ('username','is_active', 'is_superuser')
    list_filter = ('is_active','is_superuser', 'role')
    search_fields = ('user_id', 'username', 'email')
    list_per_page = 2
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations de l\'utilisateur', {
            'fields': ('email','role')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','usable_password','email', 'password1', 'password2','telephone','role',),
        }),
    )

class VehiculeInline(admin.TabularInline):
    model = Vehicule
    extra = 1
    fields = ("immatriculation", "capacite_kg")
    show_change_link = True

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ("matricule_fiscale", "adresse", "type_entreprise", "raison_social")
    search_fields = ("matricule_fiscale", "adresse", "type_entreprise")
    list_editable = ("adresse", "type_entreprise", "raison_social")
    list_per_page = 2
    readonly_fields = ('created_at', 'updated_at')
    inlines = [VehiculeInline]
    fieldsets = (
        ('Informations de l\'entreprise', {
            'fields': ('raison_social', 'matricule_fiscale', 'adresse', 'type_entreprise')
        }),
        ('Gérant de l\'entreprise', {
            'fields': ('gerant',)
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        })
    )
admin.site.register(utilisateur, UserAdmin)
admin.site.register(Entreprise, EntrepriseAdmin)
    