"""
Quick Picks Activity
"""
from random import randint

NUMBER_PER_LINE = 6
MIN_VALUE = 1
MAX_VALUE = 45

number_of_lines = int(input("How many quick picks? "))

while number_of_lines < 0:
    print("Invalid number of quick picks, try again")
    number_of_lines = int(input("How many quick picks? "))

for i in range(number_of_lines):
    # Creates an empty list of quick picks.
    quick_picks = []
    # Loops through each line and creates a random set of numbers of length NUMBER_PER_LINE.
    for j in range(NUMBER_PER_LINE):
        number = randint(MIN_VALUE,MAX_VALUE)
        # Checks if number is already in the quick picks and reruns randint().
        while number in quick_picks:
            number = randint(MIN_VALUE, MAX_VALUE)
        quick_picks.append(number)
    # Sorts final line to ascending order.
    quick_picks.sort()
    # Uses a generator function with a .join command to arrange them into a grid.
    print(" ".join(f"{number:2}" for number in quick_picks))
