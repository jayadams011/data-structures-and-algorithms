"""Write a function that returns the first instance of a repeated word."""

from hash_table import HashTable


def first_repeated_word(string):
    """Find the first repeated word."""
    checked_word = set()
    ht = HashTable()
    for word in string.split():
        if word in checked_word:
            return word
        ht.set(word, word)

