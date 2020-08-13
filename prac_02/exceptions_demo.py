"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur if the input of either the numerator or the denominator is not an integer.
2. When will a ZeroDivisionError occur?
    a ZeroDivisionError will occur if the denominator is equal to 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, with an if statement that would not attempt to use the input in any equations if it is equal to 0.

Sophie Thomas
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Cannot divide by zero, please pick a new denominator")
            denominator = int(input("Enter the denominator: "))
        else:
            valid_input = True
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
print("Finished.")

