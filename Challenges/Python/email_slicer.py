import email
import re


# STEPS
# 1. create email input & valid it
# 2. split out usermame from domain
# Next steps - read in file and break out usernames & count the most popular domain maybe by region??


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validation(email_input):
    if(re.fullmatch(regex, email_input)):
        print("Valid")
    else:
        return "Invalid"
    
print(validation(email_input= input("Please enter your email address: ")))