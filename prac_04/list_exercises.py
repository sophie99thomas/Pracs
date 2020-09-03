"""
Asks for 5 numbers and tells you fun things about those numbers.
Sophie Thomas
"""


def main():
    user_name = str(input('Username: '))
    good_name = checks_username(user_name)
    if not good_name:
        print("Access denied!")
    else:
        print("Access granted!")
        number_game()


def number_game():
    user_numbers = asks_input()
    number_strings = index_string(user_numbers)
    print(number_strings)


def asks_input():
    numbers = []
    for i in range(1, 6):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def index_string(numbers):
    first = numbers[0]
    last = numbers[-1]
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers) / len(numbers)
    string_to_print = "The first number is {}.\n" \
                      "The last number is {}.\n" \
                      "The smallest number is {}.\n" \
                      "The largest number is {}.\n" \
                      "The average of the numbers is {:.2f}.".format(first, last, smallest, largest, average)
    return string_to_print


def checks_username(name):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    for username in usernames:
        if name == username:
            return True
        else:
            pass


main()
