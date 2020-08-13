"""
Task 1
      Creates a file of your name, containing your name.
Task 2
      Opens said file and tells you what your name is.
Task 3
      Opens a different file called numbers, reads it, then adds the first two toegther.

Sophie Thomas
"""
# Task 1
name = str(input("What is your name? ").title())
name_file = name + ".txt"
name_file_out = open("{}".format(name_file), 'w')
print(name, file=name_file_out)
name_file_out.close()

# Task 2
name_file_in = open("{}".format(name_file), 'r')
Name = name_file_in.read()
print("Your name is {}".format(Name))
name_file_in.close()

# Task 3
numbers = open("numbers.txt", 'r')
number_lines = []
number_first_line = numbers.readline()
number_second_line = numbers.readline()
number_one = int(number_first_line)
number_two = int(number_second_line)
total = number_one + number_two
print("The sum of {0} and {1} is {2}\n"
      "{0} + {1} = {2}".format(number_one, number_two, total))
