# SOURCES.md

# SAP Research

Researched:
- SAP flat-file exports
- SAP CSV reporting exports
- procurement/fuel reporting formats

Learnings:
SAP exports commonly contain:
- inconsistent column names
- mixed units
- ERP-specific identifiers
- difficult formatting

Prototype Decision:
Used CSV upload simulation with normalized columns.

Potential Real-World Breakage:
- multilingual headers
- inconsistent date formats
- missing lookup mappings

---

# Utility Data Research

Researched:
- utility portal CSV exports
- electricity billing exports

Learnings:
Utility exports commonly contain:
- billing periods
- usage units
- meter identifiers

Prototype Decision:
Used CSV upload with usage and unit normalization.

Potential Real-World Breakage:
- tariff structures
- PDF-only utilities
- irregular billing cycles

---

# Travel Data Research

Researched:
- Concur export formats
- Navan travel reporting APIs

Learnings:
Travel systems commonly expose:
- travel category
- trip distances
- expense classifications

Prototype Decision:
Used CSV travel exports with Scope 3 categorization.

Potential Real-World Breakage:
- missing airport distances
- inconsistent travel categories
- hotel emissions mapping

---

# Sample Data

Created realistic sample rows for:
- fuel consumption
- electricity usage
- business travel

Also created intentionally invalid rows to test:
- failed ingestion handling
- suspicious detection
- analyst review workflows