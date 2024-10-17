from validator_collection import validators, errors

#^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
#type malan@harvard.edu, followed by Enter. Your program should output Valid.
#Type your own email, followed by Enter. Your program should output Valid.
#malan@@@harvard.edu, followed by Enter. Your program should output Invalid.
#Mistype your own email, including an extra . before .com, for example. Press enter and your program should output Invalid.

email = input("User email: ")

#if matches := re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):
#    print("Valid")
#else:
#    print("Invalid")

try:
    email_address = validators.email(email)
    print("Valid")
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")
