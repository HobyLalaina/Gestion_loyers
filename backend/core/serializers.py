from rest_framework import serializers
from .models import Locataire, Loyer

class LocataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locataire
        fields = '__all__'

class LoyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyer
        fields = '__all__'
