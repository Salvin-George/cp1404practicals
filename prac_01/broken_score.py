"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this! (Fixed ;))

score = float(input("Enter score: "))
if 100 >= score >= 90:
    print("Excellent")
elif 90 > score >= 50:
    print("Passable")
elif 50 > score >= 0:
    print("Bad")
else:
    print("Invalid score")
