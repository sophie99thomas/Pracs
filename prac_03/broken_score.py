"""
CP1404/CP5632 - Practical
Fixed score program
Sophie Thomas
"""
def main():
    score = float(input("Enter score: "))
    if score <= 0:
        print("Invalid score")
    else:
        word_to_print = score_words(score)
        print(word_to_print)


def score_words(score):
    if 100 >= score >= 90:
        return "Excellent"
    elif 90 > score >= 80:
        return "Good"
    elif 80 > score >= 50:
        return "Passable"
    elif 50 > score > 0:
        return "Bad"


main()