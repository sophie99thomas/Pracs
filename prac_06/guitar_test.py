"""
Guitar class test.
Sophie Thomas.
"""
from prac_06.guitar import Guitar
print_format = "{} is {} years old. Is vintage: {}"
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 3999.99)
third_guitar = Guitar("test name", 1844, 82938.01)
fifty_year_old = Guitar("Fifty", 1970, 5858)
print(print_format.format(gibson.name, gibson.get_age(), gibson.is_vintage()))
print(print_format.format(another_guitar.name, another_guitar.get_age(), another_guitar.is_vintage()))
print(print_format.format(third_guitar.name, third_guitar.get_age(), third_guitar.is_vintage()))
print(print_format.format(fifty_year_old.name, fifty_year_old.get_age(), fifty_year_old.is_vintage()))