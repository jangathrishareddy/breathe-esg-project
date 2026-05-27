from django.urls import path
from django.http import JsonResponse

from .views import (
    upload_data,
    get_records,
    approve_record,
    get_failed_records
)

# Root API check endpoint
def api_root(request):
    return JsonResponse({
        "message": "API working",
        "endpoints": {
            "upload": "/api/upload/",
            "records": "/api/records/",
            "approve": "/api/approve/<id>/",
            "failed_records": "/api/failed-records/"
        }
    })

urlpatterns = [
    path('', api_root),

    path('upload/', upload_data),
    path('records/', get_records),
    path('approve/<int:pk>/', approve_record),
    path('failed-records/', get_failed_records),
]