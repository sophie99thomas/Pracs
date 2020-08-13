"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
Sophie Thomas
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
NUMBERS = "1234567890"
FORMAT = "Example Format:\n" \
         "ccsvcnvvcsnc\n" \
         "Where 'c' is a consonant, 'v' is a vowel, 's' is a special character, and 'n' is a number"
format_chosen = False
# print(FORMAT)
# print()
form = str(input("Do you want to make the format yourself? Y/N ").upper())
word_format = ""

while not format_chosen:
    if form == "Y":
        print(FORMAT)
        print()
        word_format = str(input("Enter preferred password format: "))
        format_chosen = True
    elif form == "N":
        auto_format = random.choice(NUMBERS, CONSONANTS, VOWELS, SPECIAL_CHARACTERS)
    else:
        print("You tried, good job. Try again but enter either Y or N")

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "v":
        word += random.choice(VOWELS)
    elif kind == "s":
        word += random.choice(SPECIAL_CHARACTERS)
    elif kind == "n":
        word += random.choice(NUMBERS)
    else:
        print("Good job, you broke it. We're just going to pretend that input didn't happen okay?")

print(word)
