"""
Practical 07: Guitars
Estimate: 20mins
Actual:
"""
import csv

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main client program."""
    guitars = read_files(FILENAME)
    print("My guitars!")
    for guitar in guitars:
        print(guitar)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_addition = Guitar(name, year, cost)
        guitars.append(guitar_addition)
        print(f"{guitar_addition} added.")
        name = input("Name: ")

    print("------------------------------------")
    if guitars:
        print("These are my guitars:")
        guitars.sort()
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars found.")
    print(guitars)
    write_files(guitars, FILENAME)


def read_files(filename):
    """File reader using csv module"""
    guitars = []
    with open(filename, "r", encoding="UTF-8") as in_file:
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            guitars.append(guitar)
    return guitars


def write_files(guitars, filename):
    """Writes classes to a provided file"""
    with open(filename, "w", newline="", encoding="UTF-8") as out_file:
        writer = csv.writer(out_file)  # Create a CSV writer
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
