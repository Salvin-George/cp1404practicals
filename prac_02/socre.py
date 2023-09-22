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
    if 100 >= score >= 90:
        return "Excellent"
    elif 90 > score >= 50:
        return "Passable"
    elif 50 > score >= 0:
        return "Bad"
    else:
        return "Invalid score"


main()
