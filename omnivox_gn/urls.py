
from django.urls import path
from rest_framework import routers

from omnivox_gn.views import EtudiantViewSet,get_Etablissement,create_Etablissement,etablissement_Detail


# router= routers.DefaultRouter()
# router.register('Etudiant',EtudiantViewSet)
urlpatterns=[
    path('etablissements/', get_Etablissement, name='get-Etablissement'),
    path('etablissements/create/', create_Etablissement, name='create-Etablissement'),
    path('etablissements/<int:pk>', etablissement_Detail, name='etablissement-detail')
]