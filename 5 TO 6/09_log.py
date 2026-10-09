
log_data = [
    "data.txt",
    "report.pdf",
    "act.bat",
    "xyz.apk",
    "pmYojana.apk",
    "cmYojana.docs",
]

# for log in log_data:
#     if log.endswith(".apk"):
#         print("Warning...")
#         print("check this file:",log)

# for i in range(1,10):
#     print(i)

for last_octet in range(1,10):
    print(f"192.168.53.{last_octet}")