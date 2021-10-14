from .views import (
    AssetsViewSet,
    AnalystsViewSet
)

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"analysts", AnalystsViewSet, basename="analysts")
router.register(r"assets", AssetsViewSet, basename="assets")
