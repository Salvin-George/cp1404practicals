"""
Prac 2, menu score practical
"""


# noinspection PyTypeChecker
def main():
    print("Menu \n(G)et score \n(P)rint result \n(S)how stars \n(Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(print_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print("Menu \n(G)et score \n(P)rint result \n(S)how stars \n(Q)uit")
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score() -> int:
    score = int(input("Score: "))
    while 0 >= score >= 100:
        print("Invalid Name")
        score = int(input("Score: "))
    return score


def print_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * score)


main()
