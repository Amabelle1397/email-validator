print "This app validates email"

email = raw_input("Please enter your email: ")

def validate_email_char(e):

if "gmail" && "yahoo" in email:
	return true
else:
	return false

def validate_email_keywords(e):

if ".com" && "@" in email:
	return true
else:
	return false


if validate_email(email):
	print "Your email is valid"
else:
	print "Your email is invalid"
