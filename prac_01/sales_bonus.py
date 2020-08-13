"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
bonus_under = 0.1
bonus_over = 0.15

while sales >= 1:
    if sales < 1000:
        calculated_bonus = sales * bonus_under
        total = sales + calculated_bonus
        print("Your bonus is 10%: $", calculated_bonus)
        print("Total: $", total)
    elif sales >= 1000:
        calculated_bonus = sales * bonus_over
        total = sales + calculated_bonus
        print("Your bonus is 15%: $", calculated_bonus)
        print("Total: $", total)

    sales = float(input("Enter sales: $"))

print("No more sales")