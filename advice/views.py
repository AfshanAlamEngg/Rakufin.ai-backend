from rest_framework import viewsets
from .models import FinancialAdvice
from .serializers import FinancialAdviceSerializer

class FinancialAdviceViewSet(viewsets.ModelViewSet):
    queryset = FinancialAdvice.objects.all()
    serializer_class = FinancialAdviceSerializer
