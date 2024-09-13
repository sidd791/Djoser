from django.urls import path, include

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),  # Djoser URLs
    path('api/v1/auth/', include('djoser.urls.jwt')),  # Djoser JWT endpoints
]
