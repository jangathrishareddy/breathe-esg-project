from django.urls import path
from django.http import JsonResponse

from .views import upload_data, get_records, approve_record, get_failed_records

def api_root(request):
    return JsonResponse({"message": "API working"})

urlpatterns = [
    path('', api_root),
    path('upload/', upload_data),
    path('records/', get_records),
    path('approve/<int:pk>/', approve_record),
    path('failed-records/', get_failed_records),
]