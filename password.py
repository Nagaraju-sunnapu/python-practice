import re
def password(p):
    if(len(p)>7 and re.search(r"[A-Z]+",p) and re.search(r"[a-z]+",p) and re.search(r'[0-9]+',p) and 
         re.search(r'[^A-Za-z0-9]+',p) and not re.search(r'\s',p)):
        return "is valid password"
    else:
        return "is invalid password"
p=input("enter a password:")
print(password(p))