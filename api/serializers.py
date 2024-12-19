from rest_framework import serializers
from .models import Concession, Vehicule

class ConcessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        exclude = ('numero_siret',)  # Ne pas exposer le numéro SIRET

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'  # Inclure tous les champs
