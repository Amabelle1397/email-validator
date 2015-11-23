print "This app validates email"

email = raw_input("Please enter your email: ")

def validate_email_char(e)

	if "@" in email
		return True
	else:
		return False


if validate_email(e):
	print "Your email is valid"
else
	"Your email is invalid"
