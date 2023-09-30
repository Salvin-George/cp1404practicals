"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the inserted or inputted value is not of the correct type to be used (e.g. Str used in place of a int)
2. When will a ZeroDivisionError occur? whenever any mathematical operation divides any value by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")
