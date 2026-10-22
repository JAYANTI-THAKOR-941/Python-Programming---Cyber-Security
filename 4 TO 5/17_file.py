# file handling in python

# create new file and write data

# with open("info.txt","w",encoding="utf-8") as f:
#     f.write("\nField:Core Libraries & Frameworks")
#     f.write(\\nA"I & Machine Learning : nTensorFlow, PyTorch, scikit-learn")
#     f.write("\nData Science & Analytics : pandas, NumPy, Matplotlib, Seaborn")

# with open("info.txt","a",encoding="utf-8") as f:
#     f.write("\nWeb Development : Django, Flask, FastAPI")
#     f.write("\nAutomation & DevOps : System scripting, deployment tools")

# course = "Python Programming"
# duration = 4.5

# with open("info.txt","a",encoding="utf-8") as f:
#     f.write(f"\n\n{course} duration is:{duration} months.")


# read data from file

f = open("python.txt","r",encoding="utf-8")
data = f.read()
f.close()

print(data)
