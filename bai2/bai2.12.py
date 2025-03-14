print("sinh vien : Dau Duc Tu")
print("msv 235752020710009")
import re

def check_password(password):
    if (6 <= len(password) <= 12
            and re.search(r"[a-z]", password)
            and re.search(r"[0-9]", password)
            and re.search(r"[A_Z]", password)
            and re.search(r"[$#@]", password)):
        return True
    return False

# Inour=t string of passwords separated by commas
passwords = input("Enter passwords separated by comma: ")

# Split the input string into individual passwords
password_list = passwords.split(',')

#list to store valid passwords
valid_password = []

#check each password
for password in password_list:
    if check_password(password.strip()):
         valid_password.append(password.strip())

# print valid passwords separated by comma
prind(",".join(valid_passwords))
