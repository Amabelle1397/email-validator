print "This App validates Email"

email = raw_input("Please enter your email:")


def validate_email(e):
    #define codes here
    if validate_email in('@') :
        return True

    else:
        return False


def validate_email_word(e):
    #define codes here
    if validate_email in('.com') :
        return True

    else:
        return False

def validate_email_num (e) :
    #define codes here
    if validate_email in () :
        return True

    else:
        return False







if validate_email(email):
    print " Your email is valid!"
else:
    print " Your email is invalid!"
