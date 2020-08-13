print("Electricity bill estimator")

TARIFF_11 = 0.123342
TARIFF_31 = 0.388573

# cents_kWh = int(input("Enter cents per kWh: "))
tariff_number = int(input("Which tariff, 11 or 31? "))
if tariff_number == 11:
    tariff = TARIFF_11
elif tariff_number == 31:
    tariff = TARIFF_31
else:
    print("Invalid tariff")


daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billings days: "))

# estimated_bill = (cents_kWh / 100) * (daily_use * billing_days)
estimated_bill = tariff * (daily_use * billing_days)

print("Estimated Bill: $", estimated_bill)
