from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialAdviceViewSet

router = DefaultRouter()
router.register(r'financial-advice', FinancialAdviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
