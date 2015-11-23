print "This app validates email"

email = raw_input("Please enter your email: ")

def validate_email_char(e):
    if email == ".com" or "@":
        return True

def validate_email_struc(e):
    if email[-4:] ==".com":
        return True

def validate_space(e):
    if email != " ":
        return True

def validate_email(e):
  if validate_email_char(e) and validate_email_struc(e) and validate_space(e):
    return True
  else:
    return False

if validate_email(email):
    print "Your email is valid"
else:
    print "Your email is invalid"
