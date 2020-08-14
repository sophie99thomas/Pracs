def main():
    password = get_password()
    valid_password = False
    while not valid_password:
        if len(password) > 10:
            print_asterisks(password)
            valid_password = True
        else:
            print("Password too short, please try again.")
            password = str(input("Password: "))


def get_password():
    return str(input("Password: "))


def print_asterisks(number):
    print("*" * len(number))


main()
