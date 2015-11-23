print "This app validates email"

email = raw_input("Please enter your E-mail: " )

def validate_email_keywords(e):
    if "gmail" & "yahoo" in email:
        return True

def validate_email_char(e):
    if "@" & ".com" in email:
        return True


def validate_email(e):
    if validate_email_keywords(e) + validate_email_char(e) :
        return True
    else:
        return False

    if validate_email(email):
        print "Your email is valid"

    else:
        print "Your email is invalid"
