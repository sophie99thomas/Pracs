from math import sqrt, ceil

MENU = "(E)ven, \n" \
       "(O)dd, \n" \
       "(S)quares, \n" \
       "(Q)uit"

x_limit = int(input("Enter lower limit (x): "))
y_limit = int(input("Enter higher limit (y) "))
print(MENU)
choice = str.upper(input("What do you want to do? "))

while choice != "Q":
    for i in range(x_limit, y_limit + 1, 1):
        if choice == "E":
            if i % 2 == 0:
                print(i, end=' ')
        elif choice == "O":
            if i % 2 == 1:
                print(i, end=' ')
        elif choice == "S":
            i_sqrt = sqrt(i)
            if i_sqrt.is_integer():
                print(int(i_sqrt), end=' ')
        else:
            print("Invalid input")
    print()
    choice = str.upper(input("What do you want to do? "))

print("Finished.")
