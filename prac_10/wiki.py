"""
Wikipedia Practical
Esitmate: 7mins
Actual:
"""

import wikipedia

search = input("Search: ")
while search:
    try:
        page = wikipedia.summary(search, autosuggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous term. Options: {e.options}")

    search = input("Search: ")