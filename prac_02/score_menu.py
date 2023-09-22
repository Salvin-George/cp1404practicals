"""
Prac 2, menu score practical
"""


def main()
    print("Menu \n(G)et score \n(P)rint result \n(S)how stars \n(Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")

        print("Menu \n(G)et Name \n(P)rint greeting \n(S)ecret name")
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    score = int(input("Score: "))
    while 0<= score <= 100:
        print("Invalid Name")
        score = int(input("Score: "))
    return score


def print_result(score):
    if 100 >= score >= 90:
        return "Excellent"
    elif 90 > score >= 50:
        return "Passable"
    elif 50 > score >= 0:
        return "Bad"
    else:
        return "Invalid score"


def print_stars(score):
    print("*" * len(score))


main()