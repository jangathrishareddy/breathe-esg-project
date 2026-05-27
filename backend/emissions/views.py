from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord


@api_view(["POST"])
def approve_record(request, record_id):

    try:

        record = EmissionRecord.objects.get(
            id=record_id
        )

        record.status = "APPROVED"

        record.locked_for_audit = True

        record.save()

        return Response({
            "message": "Record approved"
        })

    except EmissionRecord.DoesNotExist:

        return Response({
            "error": "Record not found"
        }, status=404)