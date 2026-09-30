import re

text = " " 

email_pattern = r'[a-zA-z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}'

email = re.findall(email_pattern,text)
print("Email addresses found:")

for email in email:
    print(email)