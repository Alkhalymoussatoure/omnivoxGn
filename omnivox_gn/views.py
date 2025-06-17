from django.shortcuts import render
from rest_framework import viewsets

from .models import Etablissement,Etudiant

from .serializers import Etablissement_serialiser,Etudiant_serialiser

# cette nuit
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = Etudiant_serialiser

    
@api_view(['GET'])
def get_Etablissement(request):
    Etablissements =Etablissement.objects.all()
    donneeSerialisees =Etablissement_serialiser(Etablissements, many=True).data
    return Response(donneeSerialisees)

@api_view(['PUT'])
def create_Etablissement(request):
    donnee = request.data
    serializer = Etablissement_serialiser(data=donnee)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def etablissement_Detail(request, pk):
    try:
        etablissement = Etablissement.objects.get(pk=pk)
        
    except Etablissement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        etablissement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method =='PUT': 
        donnee = request.data
        serializer = Etablissement_serialiser(Etablissement, data=donnee)
        
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)