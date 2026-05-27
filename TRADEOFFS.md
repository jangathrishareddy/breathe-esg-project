# TRADEOFFS.md

# 1. Authentication and RBAC

Not implemented.

Reason:
The assignment prioritized ingestion pipelines and audit workflows over user management.

Future improvement:
- analyst/admin roles
- JWT authentication
- tenant isolation

---

# 2. Real SAP/API Integrations

Not implemented.

Reason:
Real SAP integrations require authentication, enterprise credentials, and large integration setup effort.

Prototype instead uses realistic CSV exports.

---

# 3. Async Processing

Not implemented.

Reason:
Current uploads are small enough for synchronous ingestion.

Future improvement:
- Celery workers
- background processing
- queue-based ingestion

---

# 4. PDF Utility Parsing

Not implemented.

Reason:
Reliable PDF extraction is time-consuming and error-prone for prototype scope.

---

# 5. Advanced Emissions Calculations

Not implemented.

Reason:
Assignment focused more on ingestion normalization and workflow design than emissions science calculations.