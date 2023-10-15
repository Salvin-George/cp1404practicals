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
        confirm = input(f"Is this your name, {name}? (Y/n)")
        if confirm.lower().strip() == "n":
            user_name = input("Name: ")
            user_email = input("Email: ")
            name_to_email[user_email] = user_name
            break
        name_to_email[email] = name
    print_emails(name_to_email)


def extract_name(email):
    name = email.split('@')[0]
    name = name.split(".")
    name = [part.capitalize() for part in name]
    name = ' '.join(name)
    return name


def print_emails(name_to_email):
    print("---")
    for email, name in name_to_email.items():
        print(f"{name.capitalize()} : {email}")


main()
