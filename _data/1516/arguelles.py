print "Validate email"

email = raw_input("enter email address: ")


def validate_email(e):
  if "@" in email:
    return True
  
  else:
    return False

def keywords_email(e):
  if ".com" in email:
    return True
  
  else:
    return False


  
if " " in email:
  return False 
else:
  return True

  

#def valid_email(email):
#if validate_email and keywords_email
#  return True
#else:
#  return False



if valid_email(email):
  print "Email is valid"
else:
  print "Your Email is invalid"

