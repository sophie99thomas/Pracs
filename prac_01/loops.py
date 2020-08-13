# Ranges
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(21, 0, -1):
    print(i, end=' ')
print()

# Stars
number_stars = int(input("How many stars do you want? "))

for i in range(number_stars, 0, -1):
    print("*", end=' ')

print()
print("Christmas Tree Stars")

for i in range(0, number_stars, 1):
    for i in range(0, i+1, 1):
        print("*", end=' ')
    print()



