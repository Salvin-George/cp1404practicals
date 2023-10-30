"""
Guitar client program
Estimate: 20mins
Actual: 18mins
"""

from guitar import Guitar


def main():
    """Main client program."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_addition = Guitar(name, year, cost)
        guitars.append(guitar_addition)
        print(f"{guitar_addition} added.")
        name = input("Name: ")

    print("------------------------------------")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars,1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars found.")

main()