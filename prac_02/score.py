"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(score_result(score))
    print(f"A random rating of {score_result(randint(1,100))} ")


def score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
