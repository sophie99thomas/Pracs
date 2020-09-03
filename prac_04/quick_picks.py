"""
Quick pick program - shows x lines of 6 random numbers between 1 and 45.
Sophie Thomas
"""
import random


def main():
    number_of_lines = int(input("How many quick picks? "))
    for i in range(1, number_of_lines + 1):
        random_numbers = generates_numbers(number_of_lines)
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(random_numbers[0], random_numbers[1], random_numbers[2],
                                                     random_numbers[3], random_numbers[4], random_numbers[5]))


def generates_numbers(number_of_lines):
    line_to_print = []
    while len(line_to_print) < 6:
        for j in range(1, 7):
            line_to_print.append(random.randint(1, 45))
            line_to_print.sort(reverse=True)
        any(line_to_print.count(x) > 1 for x in line_to_print)
    return line_to_print


main()
