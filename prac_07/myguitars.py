"""
Practical 07: Guitars
Estimate: 20mins
Actual:
"""
import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Initialises program"""
    guitars = read_files(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_files(filename):
    """File reader using csv module"""
    guitars = []
    with open(filename, "r", encoding="UTF-8") as in_file:
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            guitar = Guitar(row[0],int(row[1]),float(row[2]))
            guitars.append(guitar)
    return guitars

main()
