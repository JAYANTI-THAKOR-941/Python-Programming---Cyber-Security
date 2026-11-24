# Python for defensive cybersecurity — practice academy

Prerequisite: Python 3.10+, basic terminal skills. All exercises use synthetic data or local files. Do not point exercises at third-party systems.

| Day | Topic | Practical |
|---|---|---|
| 01 | Variables and types | Parse a fictional login event |
| 02 | Conditions | Classify event outcomes |
| 03 | Loops | Count repeated failures |
| 04 | Lists and dictionaries | Group counts by account |
| 05 | Functions | Reusable input validation |
| 06 | Exceptions | Handle missing or malformed input |
| 07 | CSV | Read synthetic event records |
| 08 | JSON | Export an analysis summary |
| 09 | Regular expressions | Validate expected local log format |
| 10 | File handling | Read and write local reports |
| 11 | Hashing | SHA-256 integrity comparison |
| 12 | IP addressing | Validate and classify example IPv4 addresses |
| 13 | Statistics | Calculate login failure rate |
| 14 | Unit testing | Verify expected output and edge cases |
| 15 | Capstone | Local defensive event review report |

## Run
From the repository root:

```sh
python academy/log_review.py academy/sample_events.csv
python academy/integrity.py academy/sample_events.csv
python -m unittest discover -s academy -p "test_*.py"
```

## Assignments
1. Add a threshold argument to flag accounts with at least three failures.
2. Reject records with missing account or outcome.
3. Compute success rate, handling empty files safely.
4. Make a copy of the sample CSV, edit it, and compare hashes.
5. Explain why a hash does not establish the source of a file.
6. Write tests for invalid IP strings and malformed event rows.

## Expected observations
The fictional sample contains five records, three failures for student01 and two successes. A threshold of three flags student01 for review, not as proof of an attack.
