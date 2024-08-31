from rest_framework import serializers
from .models import FinancialAdvice

class FinancialAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAdvice
        fields = '__all__'
