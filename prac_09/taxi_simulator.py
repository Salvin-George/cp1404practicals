"""
Taxi simulator client code
Estimate: 20mins
Actual:
"""
from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    # Menu code
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = choose_a_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                distance_to_drive = float(input("Drive how far? "))
                trip_cost = drive_taxi(current_taxi,distance_to_drive)
                total_cost += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()


    # Quit message
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display a numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_a_taxi(taxis):
    current_taxi = None #Intialises current taxi object
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    except ValueError:
        print("Please input valid integer.")
    return current_taxi


def drive_taxi(current_taxi, distance_to_drive):
    current_taxi.start_fare()
    current_taxi.drive(distance_to_drive)
    trip_cost = current_taxi.get_fare()
    return trip_cost


main()
