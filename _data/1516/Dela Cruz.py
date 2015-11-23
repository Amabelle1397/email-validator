print "This app validates email addresses."

email = raw_input("Please enter your email: ")

def validate_email(e):
    if '.com' in email and '@' in email:
        if ' ' in email:
            return False
        elif email[0] == "@":
            return False
        else:
            return True
    elif '.ph' in email and '@' in email:
        if ' ' in email:
            return False
        elif email[0] == "@":
            return False
        else:
            return True
    elif ' ' in email and '@' in email:
        return False
    elif ' ' in email:
        return False
    elif email[0] == "@":
            return False
    else:
        return False

if validate_email(email):
    print "Valid email."
else:
    print "Invalid email."
