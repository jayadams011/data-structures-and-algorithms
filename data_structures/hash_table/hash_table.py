"""Imports needed by class."""
from functools import reduce
from linked_list import LinkedList


class HashTable:
    """HashTable class."""

    def __init__(self, max_size=1024):
        """Initailizer."""
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        """Set up the key."""
        if type(key) is not str:
            raise TypeError

        # iterate through key, and convert each char to ascii char code
        # sum all char codes for a total int value
        # return => mod total by number of buckets

        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.buckets

    def set(self, key, val):
        """Create the set function."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_val: key_val[0] == key)
        if entry is not None:
            bucket.delete(entry)
        else:
            self.size += 1
        bucket.append((key, val))
        self.buckets[self.hash_key(key)] = val

    def get(self, key):
        """Return the value associated with the given key."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            return self.buckets[self.hash_key(key)]

    def remove(self, key):
        """Create the remove function."""
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
