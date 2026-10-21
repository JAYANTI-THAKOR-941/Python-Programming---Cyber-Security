# file handling

# create file and write data

# with open("data.txt","w",encoding="utf-8") as f:
#     f.write("\nTop Threats")
#     f.write("\nMalware & Ransomware: Software that locks or harms files to demand payment.")
#     f.write("\nPhishing: Fake messages meant to trick people into giving away passwords or money..")
#     f.write("\nAI-Powered Attacks: Automated tools that make cyberattacks faster and harder to spot.")

# with open("data.txt","a",encoding="utf-8") as f:
#     f.write("\n\nCommon Types of Cybersecurity")
#     f.write("\nNetwork Security: Guards internal networks from intruders and malware.")
#     f.write("\nCloud Security: Secures data and services kept on cloud platforms.")
#     f.write("\nProtects individual devices like phones, laptops, and tablets.")
#     f.write("\nApplication Security: Fixes code flaws and protects software from threats..")

# course = "Cyber Security"
# duration = 12

# with open("data.txt","a",encoding="utf-8") as f:
#     f.write(f"\n\n{course} duration is : {duration} months.")


# read data from file

f = open("cyber.txt","r",encoding="utf-8")

data = f.read()

f.close()

print(data)