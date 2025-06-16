from django.shortcuts import render
from rest_framework import viewsets
from .models import Etablissement
from .models import Etudiant
from .serializers import Etablissement_serialiser
from .serializers import Etudiant_serialiser

# Create your views here.
class EtablissementViewSet(viewsets.ModelViewSet):
    
    queryset= Etablissement.objects.all()
    serializer_class= Etablissement_serialiser

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = Etudiant_serialiser