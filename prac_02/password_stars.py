"""
Ask user for password
"""

password_length = 10


def main():
    print_lines(get_valid_password())


def get_valid_password() -> str:
    password = input("Password: ")
    while len(password) < password_length:
        print("Invalid Password")
        password = input("Password: ")
    return password


def print_lines(valid_password):
    print('*' * len(valid_password))


main()
