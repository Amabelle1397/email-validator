print "This app validates email"

email = raw_input("Please enter your email: ")

def validate_email_char(e):
    if email in ("@", ".", ".com"):
        return True
    if email in (" ", ".."):
        return False
def validate_email(e):
    if email == "egdajay":
        return True
    else:
        return False
    if validate_email(email):
        print "Your email is valid."
    else:
        print "Your email is invalid."
