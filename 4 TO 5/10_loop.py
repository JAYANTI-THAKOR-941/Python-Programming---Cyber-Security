
logFiles = [
    "report.pdf",
    "pmYojana.apk",
    "data.txt",
    "student.txt",
    "example.apk",
    "data.apk",
    "cmYojana.pdf"
]

for file in logFiles:
    if file.endswith(".apk"):
        print("\nWarning.!!")
        print("Check this file:",file)