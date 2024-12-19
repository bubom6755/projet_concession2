from django.contrib import admin
from .models import Concession, Vehicule

@admin.register(Concession)
class ConcessionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code_postal', 'adresse')  # Colonnes affichées dans la liste
    search_fields = ('nom', 'code_postal')  # Recherche rapide
    list_filter = ('code_postal',)  # Filtres sur le côté
    fields = ('nom', 'numero_siret', 'code_postal', 'adresse')  # Champs affichés dans le formulaire d'ajout/édition
    readonly_fields = ('numero_siret',)  # Rendre le champ "numero_siret" en lecture seule

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'immatriculation', 'date_mise_en_service', 'concession')
    search_fields = ('marque', 'modele', 'immatriculation')
    list_filter = ('marque', 'date_mise_en_service', 'concession')
    fields = ('marque', 'modele', 'chevaux', 'immatriculation', 'date_mise_en_service', 'concession')


admin.site.site_header = "Gestionnaire de Concessions"
admin.site.site_title = "Concession Admin"
admin.site.index_title = "Administration de la Concession"