from django.shortcuts import render
from rest_framework import viewsets
from .models import Etablissement
from .serializers import Etablissement_serialiser

# Create your views here.
class EtablissementViewSet(viewsets.ModelViewSet):
    
    queryset= Etablissement.objects.all()
    serializer_class= Etablissement_serialiser