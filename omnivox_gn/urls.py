from rest_framework import routers
from omnivox_gn.views import EtablissementViewSet


router= routers.DefaultRouter()
router.register('Etablissement',EtablissementViewSet)