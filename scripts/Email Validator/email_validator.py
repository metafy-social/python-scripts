'''
Author: smit-sms
'pip install py3dns,pyfiglet,validate-email-address' to get required libraries

USAGE
 - Run the script by 'python email_validator.py'
 - Input the email address to be validated when prompted
'''


import pyfiglet
from validate_email_address import validate_email

# printing the ascii banner
print(pyfiglet.figlet_format(" Email Validator"))

print('-' * 72)
email_id = input("Enter email address to be validated: ")
print('-' * 72)

# Verifying the email id with the smtp server to check validity
isvalid = validate_email(email_id, verify=True)

if isvalid:
    print("\n\nThe following email address is Valid.\n")
else:
    print("\n\nThe following email address is Invalid.\n")
