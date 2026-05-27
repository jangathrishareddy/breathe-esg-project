from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', lambda r: JsonResponse({"ok": True})),
]