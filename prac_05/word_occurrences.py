"""
Program to count the occurrences of words in a string
"""

words = input("String: ").split()
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_length_word = max((len(word) for word in word_to_count))

for word, count in word_to_count.items():
    print(f"{word:{max_length_word}} : {count}")

