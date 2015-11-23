print "This app validates email"

email = raw_input("Please enter your email: ")

def validate_email(e):
    for '@' in email'
        if len('@')
            return True
        else
            return False

if validate_email(email):
    print "Your email is right"
else:
    "Invalid"
