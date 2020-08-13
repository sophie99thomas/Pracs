# Shop Calculator

price = float(input("Price of item? $"))
discount = 0.1
item_count = 1
add_item = str.upper(input("Add another item? "))

while add_item == "Y":
    new_price = float(input("Price of item? $"))
    price += new_price
    item_count += 1
    add_item = str(input("Add another item? "))

if price >= 100:
    price -= (price * discount)

print("Number of Items: ", item_count)
print("Total price: $", price)
