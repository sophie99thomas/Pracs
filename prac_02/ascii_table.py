"""
ASCII to Character Conversion Program
Sophie Thomas
"""
MENU = "(C)haracter to ACSII\n" \
       "(N)umber to character\n" \
       "(T)able"
LOWER_LIMIT = 33
UPPER_LIMIT = 127
completed = False

while not completed:
    print(MENU)
    conversion_type = str(input("What type of conversion would you like? ").upper())
    if conversion_type == "C":
        chr_input = str(input("Enter a character: "))
        ascii_out = ord(chr_input)
        print("The ASCII code for {} is {}.".format(chr_input, ascii_out))
        completed = True
    elif conversion_type == "N":
        num_input = int(input("Enter a number between 33 and 127: "))
        if LOWER_LIMIT <= num_input <= UPPER_LIMIT:
            chr_output = chr(num_input)
            print("The character for {} is {}.".format(num_input, chr_output))
            completed = True
        else:
            print("Invalid input, please try again")
            num_input = int(input("Enter a number between 33 and 127: "))
    elif conversion_type == "T":
        for i in range(LOWER_LIMIT, UPPER_LIMIT):
            j = chr(i)
            print("{:4.0f} {:4s}".format(i, j))
            completed = True
    else:
        print("Invalid option, try again")
        print(MENU)
        conversion_type = str(input("What type of conversion would you like? ").upper)

    again = str(input("Again? Y/N: ").upper())
    if again == "Y":
        completed = False
    else:
        pass
