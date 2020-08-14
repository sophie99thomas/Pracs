"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))

if score <= 0:
    print("Invalid score")
else:
    if 100 >= score >= 90:
        print("Excellent")
    elif 90 > score >= 80:
        print("Good")
    elif 80 > score >= 50:
        print("Passable")
    elif 50 > score > 0:
        print("Bad")
