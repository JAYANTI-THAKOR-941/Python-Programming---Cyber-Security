# Python for Cybersecurity — defensive practice path

Run all examples with Python 3.10+ from this directory. The examples use only local sample files, no network requests or external targets.

| Module | Topics | Practical |
|---|---|---|
| 1 | Variables, strings, conditions | Validate fictional event fields |
| 2 | Loops, collections, functions | Count events by category |
| 3 | Exceptions and files | Handle malformed CSV records |
| 4 | Hashing and integrity | Compare SHA-256 digests |
| 5 | Log analysis | Review synthetic authentication failures |
| 6 | Reporting and testing | Export summaries and write unit tests |

Commands: python log_review.py sample_events.csv; python integrity.py sample_events.csv; python -m unittest test_learning.py.

Repeated failures are a review signal, not proof of compromise. Hashes alone do not establish authenticity. Never use real credentials or sensitive logs in a public repository.
