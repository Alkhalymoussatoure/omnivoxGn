
from rest_framework import routers
from omnivox_gn.views import EtablissementViewSet
from omnivox_gn.views import EtudiantViewSet


router= routers.DefaultRouter()
router.register('Etablissement',EtablissementViewSet)
router.register('Etudiant',EtudiantViewSet)