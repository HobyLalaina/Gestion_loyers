from rest_framework import routers
from .views import LocataireViewSet, LoyerViewSet

router = routers.DefaultRouter()
router.register(r'locataires', LocataireViewSet)
router.register(r'loyers', LoyerViewSet)

urlpatterns = router.urls
