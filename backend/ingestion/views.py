import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from emissions.models import (
    Company,
    DataSource,
    EmissionRecord,
    FailedRecord
)

from audit.models import AuditLog

from emissions.serializers import (
    EmissionRecordSerializer
)


def normalize_unit(value, unit):

    unit = str(unit).lower().strip()

    if unit == "l":
        return value, "liters"

    if unit == "kwh":
        return value, "kwh"

    if unit == "km":
        return value, "km"

    return value, unit


def clean_row_data(row):

    return {
        k: (
            None if pd.isna(v)
            else str(v)
        )
        for k, v in row.to_dict().items()
    }


@api_view(['POST'])
def upload_data(request):

    try:

        csv_file = request.FILES.get('file')

        if not csv_file:

            return Response({
                "message": "No file uploaded"
            }, status=400)

        source_type = request.data.get('source_type')

        df = pd.read_csv(csv_file)

        df.columns = df.columns.str.strip().str.lower()

        company, created = Company.objects.get_or_create(
            name="Demo Company"
        )

        source = DataSource.objects.create(
            company=company,
            source_type=source_type
        )

        records_created = 0

        failed_records = 0

        for _, row in df.iterrows():

            try:

                category = str(
                    row.get('category', '')
                ).strip()

                scope = str(
                    row.get('scope', '')
                ).strip()

                value = row.get('value')

                unit = str(
                    row.get('unit', '')
                ).strip()

                # Validation

                if (
                    category == ''
                    or category == 'nan'
                    or scope == ''
                    or scope == 'nan'
                ):

                    FailedRecord.objects.create(

                        source_type=source_type,

                        raw_data=clean_row_data(row),

                        error_message="Missing category or scope"

                    )

                    failed_records += 1

                    continue

                if pd.isna(value):

                    FailedRecord.objects.create(

                        source_type=source_type,

                        raw_data=clean_row_data(row),

                        error_message="Missing value"

                    )

                    failed_records += 1

                    continue

                if (
                    unit == ''
                    or unit == 'nan'
                ):

                    FailedRecord.objects.create(

                        source_type=source_type,

                        raw_data=clean_row_data(row),

                        error_message="Missing unit"

                    )

                    failed_records += 1

                    continue

                raw_value = float(value)

                normalized_value, normalized_unit = normalize_unit(
                    raw_value,
                    unit
                )

                suspicious = False

                if raw_value > 100000:
                    suspicious = True

                record, created = EmissionRecord.objects.get_or_create(

                    company=company,

                    category=category,

                    scope=scope,

                    raw_value=raw_value,

                    raw_unit=unit,

                    defaults={

                        "source": source,

                        "normalized_value": normalized_value,

                        "normalized_unit": normalized_unit,

                        "is_suspicious": suspicious,

                        "original_row_data": clean_row_data(row)

                    }

                )

                if created:

                    AuditLog.objects.create(
                        record=record,
                        action="Record Created"
                    )

                    records_created += 1

            except Exception as e:

                print("ROW ERROR:", e)

                FailedRecord.objects.create(

                    source_type=source_type,

                    raw_data=clean_row_data(row),

                    error_message=str(e)

                )

                failed_records += 1

        return Response({

            "message": "Upload Successful",

            "records_created": records_created,

            "failed_records": failed_records

        })

    except Exception as e:

        print("UPLOAD ERROR:", e)

        return Response({

            "message": str(e)

        }, status=500)


@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all().order_by(
        '-created_at'
    )

    serializer = EmissionRecordSerializer(
        records,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def approve_record(request, pk):

    try:

        record = EmissionRecord.objects.get(id=pk)

        record.status = "APPROVED"

        record.locked_for_audit = True

        record.save()

        AuditLog.objects.create(
            record=record,
            action="Record Approved"
        )

        return Response({
            "message": "Record Approved"
        })

    except Exception:

        return Response({
            "message": "Record Not Found"
        })


@api_view(['GET'])
def get_failed_records(request):

    failed_records = FailedRecord.objects.all().order_by(
        '-created_at'
    )

    data = []

    for record in failed_records:

        data.append({

            "id": record.id,

            "source_type": record.source_type,

            "raw_data": record.raw_data,

            "error_message": record.error_message

        })

    return Response(data)