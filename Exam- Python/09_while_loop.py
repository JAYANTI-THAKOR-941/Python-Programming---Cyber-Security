"""
Program 09 : while Loop (Login Attempts Limit)  [NEW]
Cyber Expert : Jayanti Thakor

Definition:
    while loop tab tak chalta hai jab tak condition True rahe.
    Jab number of repetitions pehle se pata na ho tab while use karte hai.
    Brute-force attack se bachne ke liye login attempts limit kiye jate hai.
"""

correct_password = "admin@123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password:")
    attempts += 1
    if password == correct_password:
        print("Login Successfully.!")
        break
    else:
        print(f"Wrong password. Attempts left: {max_attempts - attempts}")
else:
    print("Account Locked.! Too many wrong attempts.")

# Output (3 baar galat password):
# Wrong password. Attempts left: 2
# Wrong password. Attempts left: 1
# Wrong password. Attempts left: 0
# Account Locked.! Too many wrong attempts.
