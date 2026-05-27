from django.urls import path

from .views import (
    upload_data,
    get_records,
    approve_record,
    get_failed_records
)

urlpatterns = [

    path(
        'upload/',
        upload_data
    ),

    path(
        'records/',
        get_records
    ),

    path(
        'approve/<int:pk>/',
        approve_record
    ),

    path(
        'failed-records/',
        get_failed_records
    ),

]