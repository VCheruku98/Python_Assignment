import re

def check_password(password): #length
    if len(password) < 8:
        print("Less than 8 characters")
        return False
    
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password): #lowerupper
        print("No Upper or lower")
        return False
    
    if not any(c.isdigit() for c in password):#digitcheck
       print("No number")
       return False
    
    if not any(c in "!,@,#,$,%" for c in password): #characters
        print("No characters")
        return False

    return True

user_password = input("Please enter your password: ") #password input

if check_password(user_password): 
    print("Password is strong")
else:
    print("Password is weak.")
