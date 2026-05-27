from django.db import models

# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.source_type


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=100)

    scope = models.CharField(max_length=20)

    raw_value = models.FloatField()

    raw_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField()

    normalized_unit = models.CharField(max_length=50)

    is_suspicious = models.BooleanField(default=False)

    original_row_data = models.JSONField(default=dict)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    locked_for_audit = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.category} - {self.status}"
        class Meta:

            constraints = [

                models.UniqueConstraint(

                    fields=[
                        'company',
                        'category',
                        'scope',
                        'raw_value',
                        'raw_unit'
                    ],

                    name='unique_emission_record'

                )

            ]
class FailedRecord(models.Model):

    source_type = models.CharField(
        max_length=100
    )

    raw_data = models.JSONField()

    error_message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.error_message
