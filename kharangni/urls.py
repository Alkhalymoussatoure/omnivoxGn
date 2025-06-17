from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from rest_framework import routers
# from omnivox_gn.urls import router as routeEtablissement

# router =routers.DefaultRouter()
# router.registry.extend(routeEtablissement.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls)),
    path('api/', include('omnivox_gn.urls')),
]
