print "This app validates your email"

email = raw_input("Please enter your email: ")

def validate_email(e):
    #define your codes here
    if "Amabelle" == email :
      return True
    else:
      return False
validate_email(email):

if validate_email(email):
    print "Your email is valid"
else:
    print "Your email is invalid"
