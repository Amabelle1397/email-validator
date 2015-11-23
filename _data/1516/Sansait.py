#Email Validator by A. Frederick Sansait 11/17/2015

print "This app validates email!"

email = raw_input("Please enter your email: ")
def validate_ampersand(e):
    if email == "@":
        return True
def validate_name (e):
    if email == "gmail" or "yahoo" or "hotmail":
        return True

def validate_dot(e):
    if email == ".":
        return True

def validate_com(e):
    if email == "com":
        return True

def validate_email(e):
    #codes defined
    if validate_dot(e) or validate_name(e) or  validate_com(e) or validate_ampersand(e):
        return True
    else:
        return False

if validate_email(email):
    print "Your email is valid"
else:
    print "Your email is invalid"
