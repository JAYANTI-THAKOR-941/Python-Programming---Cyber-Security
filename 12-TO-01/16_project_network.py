 # Day 17: Report Generator

import getpass
import os
import platform
import shutil
import socket
from datetime import datetime

# 1. Collect details automatically
now = datetime.now()
hostname = socket.gethostname()
user = getpass.getuser()
os_name = f"{platform.system()} {platform.release()}"
cpu_cores = os.cpu_count()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("10.255.255.255", 1))      # nothing is sent
    local_ip = s.getsockname()[0]
except OSError:
    local_ip = "127.0.0.1"
s.close()

total, used, free = shutil.disk_usage(os.path.abspath(os.sep))
free_percent = free / total * 100

# Check risky ports on THIS computer only
risky = {21: "FTP", 23: "Telnet", 3389: "RDP"}
open_risky = []
for port, name in risky.items():
    t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    t.settimeout(0.3)
    if t.connect_ex(("127.0.0.1", port)) == 0:
        open_risky.append(f"{name} (port {port})")
    t.close()

# 2. Create the findings automatically
findings = []
if free_percent < 10:
    findings.append(f"Low disk space: {free_percent:.1f}% free")
for item in open_risky:
    findings.append(f"Risky service open: {item}")

# 3. Format the report
lines = []
lines.append("=" * 40)
lines.append("  AUTOMATIC SYSTEM REPORT")
lines.append("=" * 40)
lines.append(f"Generated:  {now.strftime('%Y-%m-%d %H:%M:%S')}")
lines.append(f"Computer:   {hostname}")
lines.append(f"User:       {user}")
lines.append(f"OS:         {os_name}")
lines.append(f"CPU cores:  {cpu_cores}")
lines.append(f"IP address: {local_ip}")
lines.append(f"Disk free:  {free / 2**30:.1f} GB of {total / 2**30:.1f} GB")
lines.append("")
lines.append("FINDINGS")
lines.append("-" * 40)
if len(findings) == 0:
    lines.append("No problems found.")
for number, text in enumerate(findings, start=1):
    lines.append(f"{number}. {text}")
report = "\n".join(lines) + "\n"

print(report)

# 4. Save with the date and time in the file name
filename = "report_" + now.strftime("%Y%m%d_%H%M%S") + ".txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(report)
print("Saved to", filename)

# 5. Test: read it back
with open(filename, "r", encoding="utf-8") as f:
    saved = f.read()
print("Test PASSED" if saved == report else "Test FAILED")