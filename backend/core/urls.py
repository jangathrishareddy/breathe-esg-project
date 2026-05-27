from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({"status": "API working"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', test_api),
]