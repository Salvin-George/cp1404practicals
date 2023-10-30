"""
file reading and formatting
Estimate: 40mins
Actual: 60mins
"""

FILENAME = "wimbledon.csv"


def main():
    formatted_data = read_file(FILENAME)
    champion_count, countries = get_champion_stats(formatted_data)
    display_countries(champion_count, countries)


def read_file(FILENAME):
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            if line.strip():
                parts = line.split(',')
                year, champion_country, champion, runner_up_country, runner_up, score = parts[:6]
                data.append([champion, champion_country])
    return data


def get_champion_stats(formatted_data):
    champion_count = {}
    country_set = set()
    for champion, country in formatted_data:
        champion_count[champion] = champion_count.get(champion, 0) + 1
        country_set.add(country)
    return champion_count, sorted(country_set)


def display_countries(champion_count, countries):
    number_of_countries = len(countries)
    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} : {count}")
    print(f"\nThese {number_of_countries} countries have won Wimbledon:")
    print(', '.join(countries))


main()