from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', drf_views.obtain_auth_token),
    path('api/', include('my_admin.urls')),
    path('api/', include('user.urls')),
    path('api/', include('group.urls')),
    path('api/', include('gen_ai.urls')),
    path('api/', include('assets.urls')),
    path('api/', include('advice.urls')),
]
