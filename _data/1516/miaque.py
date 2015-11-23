print "this app validates email"


email = raw_input("please enter your email: ")

def validate_email(e):
    
    if "@" in email:
        return True
    if ".com" in email:
        return True
    if "_" in email:
        return True
    else:
        return False

if validate_email(email):
    print "your email is valid"
else:
    print "your email is invalid"
