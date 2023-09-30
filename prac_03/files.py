"""
Files Practice
"""

# Question 1
name = input("Name: ")
with open(f"{name}.txt", "w") as out_file:
    print(name, file=out_file)

# Question 2

with open(f"{name}.txt", "r") as in_file:
    print(in_file.read().strip())

# Question 3

with open("numbers.txt", "r") as in_file:
    number_1 = int(in_file.readline().strip())
    number_2 = int(in_file.readline().strip())
    total = number_1 + number_2
    print(total)

# Question 4
    with open("numbers.txt", "r") as in_file:
        total = 0
        for line in in_file:
            number = int(line)
            total += number
    print(total)
