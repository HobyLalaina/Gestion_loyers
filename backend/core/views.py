from rest_framework import viewsets
from .models import Locataire, Loyer
from .serializers import LocataireSerializer, LoyerSerializer

class LocataireViewSet(viewsets.ModelViewSet):
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer

class LoyerViewSet(viewsets.ModelViewSet):
    queryset = Loyer.objects.all()
    serializer_class = LoyerSerializer
