"""
file reading and formatting
Estimate: 40mins
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    formatted_data = read_file(FILENAME)


def read_file(FILENAME):
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            if line.strip():
                champion, country = line.split(",")
                data.append([champion, country])
    return data

