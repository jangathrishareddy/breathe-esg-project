# DECISIONS.md

# Ingestion Strategy

## SAP Data

Chosen Format:
CSV flat-file export

Reason:
Real SAP exports are commonly downloaded as CSV/Excel exports from reporting systems.

Ignored:
- IDoc parsing
- BAPI integration
- OData authentication

Reason:
Too large in scope for a 4-day prototype.

---

## Utility Data

Chosen Format:
CSV portal export

Reason:
Facilities teams commonly export monthly electricity usage from utility portals into CSV format.

Handled:
- billing usage values
- units
- billing categories

Ignored:
- PDF bill parsing
- tariff calculations

---

## Travel Data

Chosen Format:
CSV export simulating Concur/Navan exports

Reason:
Travel platforms commonly expose CSV exports or APIs containing:
- trip category
- distance
- travel type

Handled:
- flight distance
- travel categories

Ignored:
- airport code distance calculations
- hotel stay emissions

---

# Frontend Decisions

Used React with Bootstrap.

Reason:
Fastest way to build a clean analyst-facing dashboard within assignment constraints.

---

# Backend Decisions

Used Django REST Framework.

Reason:
Fast API development and clean ORM modeling.

---

# Suspicious Detection Logic

Current Rule:
value > 100000

Reason:
Simple heuristic prototype for analyst review.

---

# Failed Record Handling

Invalid rows are stored separately instead of rejected silently.

Reason:
Enterprise ingestion systems should preserve problematic rows for analyst investigation.

---

# Audit Locking

Approved records become locked_for_audit = True.

Reason:
Prevents modification after analyst approval.