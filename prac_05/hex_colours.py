"""
Hex name to Code dictionary practice
"""

HEX_NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                    "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                    "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}
hex_name = input("Enter name: ").lower()
while hex_name != "":
    try:
        print(hex_name, "is", HEX_NAME_TO_CODE[hex_name])
    except KeyError:
        print("Invalid Hex colour name")
    hex_name = input("Enter name: ").lower()

