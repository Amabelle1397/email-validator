print "this app validates email"

email = raw_input("please enter your email: ")

def validate_email(e):
    if  "@yahoo.com" in email:
        return True


    if  "@gmail.com" in email:
        return True


    if "@myspace.com" in email:
        return True

    if "@wvsu.edu.ph" in email:
        return True

    else:
        return False



def validate_email(e):
    if  " " in email:
        return False


    if  "/" in email:
        return False


    if "#" in email:
        return False

    if "+" in email:
        return False

    if "*" in email:
        return False

    else:
        return True

if validate_email(email):
    print "your email is valid"
else:
    print "your email is invalid"
