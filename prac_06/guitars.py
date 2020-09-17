"""
Guitars testing using Guitar class.
Sophie Thomas.
"""
from prac_06.guitar import Guitar


def main():
    guitars = []
    blank_input = False
    while not blank_input:
        new_guitar = input_guitar()
        if not new_guitar:
            blank_input = True
        else:
            guitars.append(new_guitar)
    print_guitar_list(guitars)


def input_guitar():
    try:
        name = str(input("Name: "))
        year = int(input("Year: "))
        cost = int(input("Cost : $"))
        return Guitar(name, year, cost)
    except ValueError:
        return False


def print_guitar_list(guitars):
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:10} ({}), worth ${:.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                              vintage_string))


main()
