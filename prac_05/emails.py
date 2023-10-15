"""
Email dictionary
Estimate: 30mins
Actual:
"""


def main():
    name_to_email = {}
    while True:
        email = input("Please enter your email: ")
        if email == '':
            break
        name = extract_name(email)
        print(f"Extracted name: {name}")


def extract_name(email):
    name = email.split('@')[0]
    name = name.split(".")
    name = [part.capitalize() for part in name]
    name = ' '.join(name)
    return name


main()

