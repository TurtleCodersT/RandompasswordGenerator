import string
import random
alphabet = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["!", "@", "#", "$", "%", "^", "(", ")", "[", "]", "?"]
combined = alphabet + numbers + symbols
numberofcharacters = random.randint(7, 12)
start = input("Press anything and then enter to get a password:")
password = []
for char in range(1, numberofcharacters + 1):
    password += random.choice(combined)
final_pass = ''.join(password)
print(f"Your password is {final_pass}")