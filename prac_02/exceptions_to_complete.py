"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task

Calculates annual income from weekly income.
Sophie Thomas
"""

finished = False
# result = 0
while not finished:
    try:
        weekly_income = float(input("What is your weekly income? $"))
        if weekly_income <= 0:
            print("Invalid income, please try again")
            income = float(input("What is your weekly income? $"))
        else:
            annual_income = weekly_income * 52
            finished = True
    except ValueError:
        print("Please enter a valid integer.")
# print("Valid result is:", result)
print("From a weekly income of ${:,.2f}, your annual income would be ${:,.2f}".format(weekly_income, annual_income))
