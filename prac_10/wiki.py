"""
Wikipedia Practical
Esitmate: 7mins
Actual:
"""

import wikipedia

search = input("Search: ")
while search:
    try:
        summary = wikipedia.summary(search)
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous term. Options: {e.options}")
