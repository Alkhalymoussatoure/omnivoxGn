from rest_framework import serializers
from omnivox_gn.models import Etablissement
from omnivox_gn.models import Etudiant

class Etablissement_serialiser(serializers.ModelSerializer):
     class Meta:
         model= Etablissement
         fields='__all__'

class Etudiant_serialiser(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
