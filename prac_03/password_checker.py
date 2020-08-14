password = str(input("Password: "))
valid_password = False

while not valid_password:
    if len(password) > 10:
        print("*" * len(password))
        valid_password = True
    else:
        print("Password too short, please try again.")
        password = str(input("Password: "))