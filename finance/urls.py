from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AccountViewSet, CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register("accounts", AccountViewSet, basename="account")
router.register("categories", CategoryViewSet, basename="category")
router.register("transactions", TransactionViewSet, basename="transaction")

urlpatterns = router.urls
