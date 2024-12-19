from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from .views import ConcessionViewSet, VehiculeViewSet

# Root router
router = SimpleRouter()
router.register(r'concessions', ConcessionViewSet, basename='concession')
router.register(r'vehicules', VehiculeViewSet, basename='vehicule')  # Route globale pour les véhicules

# Nested router
concession_router = NestedSimpleRouter(router, r'concessions', lookup='concession')
concession_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

urlpatterns = router.urls + concession_router.urls
