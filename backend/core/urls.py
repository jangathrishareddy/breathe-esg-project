from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

urlpatterns = [
    path('', lambda r: JsonResponse({"status": "root working"})),
    path('admin/', admin.site.urls),
    path('api/', lambda r: JsonResponse({"status": "api root working"})),
]