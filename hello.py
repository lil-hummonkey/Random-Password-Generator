PasswordLet = []
PasswordNum = []
username = input("Enter Username:")
print("Usename is: " + username)
username = input("Enter Password:")
import string
import random
for i in range(1, 12):
    PasswordLet.extend(random.choice(string.ascii_letters))
    PasswordLet.insert(random.randint(0, len(PasswordLet)) ,random.randint(1,9))
print(PasswordLet)



