# MODEL.md

## Overview

The system is designed to ingest ESG-related emissions data from multiple enterprise data sources and normalize it into a unified structure for analyst review and audit approval.

The backend uses Django ORM with PostgreSQL/SQLite compatibility.

---

# Core Models

## Company

Represents a tenant/company using the platform.

Fields:
- name

Purpose:
Supports multi-tenancy by linking all records and data sources to a company.

---

## DataSource

Represents the origin of uploaded data.

Fields:
- company
- source_type
- uploaded_at

Purpose:
Tracks where records came from:
- SAP
- Utility
- Travel

This enables source-of-truth tracking and auditability.

---

## EmissionRecord

Stores normalized ESG activity data.

Fields:
- company
- source
- category
- scope
- raw_value
- raw_unit
- normalized_value
- normalized_unit
- status
- is_suspicious
- locked_for_audit
- original_row_data
- created_at

Purpose:
Central normalized emissions table used for analyst review and audit workflows.

---

# Scope Categorization

Supported:
- Scope 1
- Scope 2
- Scope 3

Examples:
- Fuel combustion → Scope 1
- Electricity → Scope 2
- Business travel → Scope 3

---

# Unit Normalization

Raw uploaded units are normalized into standard representations.

Examples:
- l → liters
- kwh → kwh
- km → km

Normalization occurs during ingestion.

---

# Audit Trail

AuditLog tracks record lifecycle events.

Examples:
- Record Created
- Record Approved

This supports traceability before audit lock.

---

# Failed Records

Invalid rows are stored separately in FailedRecord.

Examples:
- Missing category
- Missing scope
- Missing value
- Missing unit

Purpose:
Prevents silent ingestion failures and allows analyst review.

---

# Suspicious Detection

Rows with unusually large values are flagged.

Current rule:
- value > 100000

Purpose:
Helps analysts identify potentially incorrect uploads.

---

# Approval Workflow

Analysts can approve records.

When approved:
- status = APPROVED
- locked_for_audit = True

Purpose:
Prevents modification after review.

---

# Duplicate Prevention

The system uses get_or_create() during ingestion to reduce duplicate uploads.