from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('acervo.urls')),
=======
    path('api/', include('acervo.api_urls')),
>>>>>>> f1b9b19 (feature: implementa API)
]