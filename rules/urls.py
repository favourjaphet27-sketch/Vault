from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RuleViewSet

router = DefaultRouter()
router.register(r"rules", RuleViewSet, basename="rule")

urlpatterns = router.urls
