# program for demonstrating the email validations by using the regular expressions
import re
def email_validation(mail):
	if re.findall(r'[A-Za-z0-9]@[A-za-z0-9]+.com',mail):
		return "valid email"
	else:
		return "invalid email"
mail=input("enter a mail:")
print(email_validation(mail))