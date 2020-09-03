"""
Warm up. What values do the follow expressions have?
Sophie Thomas
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]    returns 3
# numbers[-1]   returns 2
# numbers[3]    return 1
# numbers[:-1]  returns [3, 1, 4, 1, 5, 9]
# numbers[3:4]  returns 1
# 5 in numbers  returns True
# 7 in numbers  #returns False
# "3" in numbers    #returns False
# numbers + [6, 5, 3]   #returns [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers_changed = ["ten", 1, 4, 1, 5, 9, 1]

print(numbers_changed[2:])  # returns all elements except the first two.
print("9 is an element of numbers? {}".format(9 in numbers_changed)) # checks if 9 is an element of numbers_changed
