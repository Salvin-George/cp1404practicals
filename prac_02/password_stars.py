"""
Ask user for password
"""

password_length = 10


def main():
    valid_password = get_valid_password()
    print_lines(valid_password)


def get_valid_password():
    password = input("Password: ")
    while len(password) < 10:
        print("Invalid Password")
        password = input("Password: ")
    return password


def print_lines(valid_password):
    print('*' * len(valid_password))


main()
