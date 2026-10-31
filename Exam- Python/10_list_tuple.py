"""
Program 10 : List and Tuple (Port Policy Auditor)
Cyber Expert : Jayanti Thakor

Definition:
    List   = ordered, changeable (mutable) collection. Symbol : [ ]
             Methods : append(), remove(), sort()
    Tuple  = ordered, unchangeable (immutable) collection. Symbol : ( )
    Fixed data (jaise allowed ports) tuple me rakhte hai.
"""

ALLOWED_PORT = (22, 80, 443)                       # tuple
open_ports = [80, 3389, 443, 21, 22, 8080]         # list

allowed_found = []
unexpected = []

for port in open_ports:
    if port in ALLOWED_PORT:
        allowed_found.append(port)
    else:
        unexpected.append(port)

unexpected.sort()

print("=" * 30)
print("PORT POLICY AUDITOR")
print("=" * 30)
print("Total Open Ports      :", len(open_ports))
print("Total Allowed Ports   :", len(allowed_found))
print("Total Unexpected Ports:", len(unexpected))

for i, port in enumerate(unexpected, start=1):
    print(f"{i}. PORT: {port}")

# Output:
# ==============================
# PORT POLICY AUDITOR
# ==============================
# Total Open Ports      : 6
# Total Allowed Ports   : 3
# Total Unexpected Ports: 3
# 1. PORT: 21
# 2. PORT: 3389
# 3. PORT: 8080
