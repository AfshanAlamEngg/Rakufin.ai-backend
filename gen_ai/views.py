from rest_framework import viewsets
from .models import FinancialAdvice
from .serializers import FinancialAdviceSerializer
import openai
from django.conf import settings

openai.api_key = settings.AZURE_OPENAI_API_KEY

class FinancialAdviceViewSet(viewsets.ModelViewSet):
    queryset = FinancialAdvice.objects.all()
    serializer_class = FinancialAdviceSerializer

    def create(self, request, *args, **kwargs):
        user_age = request.data.get('user_age')
        target_asset = request.data.get('target_asset')
        target_value = request.data.get('target_value')
        target_age = request.data.get('target_age')

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial advisor."},
                {"role": "user", "content": f"I am currently {user_age} years old, plan to invest in {target_asset} with a target value of {target_value} by {target_age}, provide financial advice."}
            ]
        )

        advice = response.choices[0].message.content
        advice_obj = FinancialAdvice.objects.create(user=request.user, advice_text=advice)
        serializer = self.get_serializer(advice_obj)

        return JsonResponse(serializer.data, status=201)
