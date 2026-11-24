from django.contrib import admin
from .models import Offre
import csv
from django.http import HttpResponse
@admin.action(description="Exporter la sélection en CSV")
def exporter_offres_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="offres.csv"'
    writer = csv.writer(response)
    writer.writerow(['reference_expedition', 'vehicule', 'prix'])
    for offre in queryset.select_related('expedition', 'vehicule'):
        writer.writerow([offre.expedition.reference, offre.vehicule.immatriculation,offre.prix])
    return response

@admin.action(description="Changer le statut de l'offre à accepté")
def changer_status_accepte(modeladmin, request, queryset):
    queryset.update(statut='a')

class PrixFilter(admin.SimpleListFilter):
    title = 'Prix'
    parameter_name = 'prix'

    def lookups(self, request, model_admin):
        return [
            ('moins_100', 'Moins de 100'),
            ('entre_100_et_1000', 'Entre 100 et 1000'),
            ('plus_1000', 'Plus de 1000'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'moins_100':
            return queryset.filter(prix__lt=100)
        if self.value() == 'entre_100_et_1000':
            return queryset.filter(prix__gte=100, prix__lte=1000)
        if self.value() == 'plus_1000':
            return queryset.filter(prix__gt=1000)
        return queryset

class OffreAdmin(admin.ModelAdmin):
    actions = [exporter_offres_csv, changer_status_accepte]
    list_display = ('prix', 'delai_jours', 'statut', 'date_proposition', 'created_at', 'updated_at', 'expedition', 'entreprise', 'vehicule')
    list_filter = ('statut', 'date_proposition', 'created_at', 'updated_at', PrixFilter)
    search_fields = ('prix', 'delai_jours', 'statut', 'expedition__id', 'entreprise__id', 'vehicule__id')
    list_editable = ('statut',)
    list_per_page = 10
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ("Informations de l'offre", {
        'fields': ('prix', 'delai_jours', 'statut')
        }),
        ('Expédition associée', {
            'fields': ('expedition',)
        }),
        ('Entreprise associée', {
            'fields': ('entreprise',)
        }),
        ('Véhicule associé', {
            'fields': ('vehicule',)
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            }),
    )
admin.site.register(Offre, OffreAdmin)