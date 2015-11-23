print "This app validates email"

email = raw_input("Please enter your email: ")

def validate_email(e):

    if "@" in email:
        return True
    if "_" in email:
        return True
        if ".com" in email:
            return True

    if " " in email:
        return False

if validate_email(email):
    print "Your email is valid"
else:
    print "Your email is invalid"
