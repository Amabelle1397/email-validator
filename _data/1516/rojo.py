print "This app validates email. like for real!"

email = raw_input("Enter email:")


def validates_email(e):
    if email == email in('.com'):
        return True
    else:
        return False



if validates_email(email):
    print'your email is real.'
else :
    print 'Your email is invalid...'
