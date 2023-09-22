"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print(f"Result: {celsius_to_fahrenheit():.2f} F")
        elif choice == "F":
            print(f"Result: {fahrenheit_to_celsius():.2f} F")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit() -> float:
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius() -> float:
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit-32)
    return celsius


main()
