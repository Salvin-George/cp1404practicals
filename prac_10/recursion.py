"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# Q1:
'(1+0+1+0+1)'
'output: 3'
# Q2:
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print('Invalid starting number')
    for i in range(n,-1,-1):
        print(i**2)


# Q3:
1
4
9
16
25
...
# Q4:
do_something(4)
