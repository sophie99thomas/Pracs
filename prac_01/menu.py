

MENU = "(H)ello \n" \
       "(G)oodbye \n" \
       "(Q)uit"

name = str(input("What is your name? "))
print("Thank-you", name, "pick one of the following options:")
print(MENU)
choice = str.upper(input(">>> "))

while choice != "Q":
    if choice == "H":
        print("Hello!", name)
    elif choice == "G":
        print("Goodbye!", name)
    else:
        print("Invalid Message")
    print(MENU)
    choice = str.upper(input(">>>"))

print("Finished. Thanks for playing")
