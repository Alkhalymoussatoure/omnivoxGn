from rest_framework import serializers
from omnivox_gn.models import Etablissement

class Etablissement_serialiser(serializers.ModelSerializer):
     class Meta:
         model= Etablissement
         fields='__all__'
        