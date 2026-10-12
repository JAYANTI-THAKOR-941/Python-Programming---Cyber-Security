# loop in python

logFiles = [
    "base.bat",
    "pmYojana.apk",
    "data.txt",
    "cmYojana.pdf",
    "demo.apk",
    "python.pdf"
]

for file in logFiles:
    if file.endswith(".apk"):
        print("Warning...!")
        print("Check This file:",file)