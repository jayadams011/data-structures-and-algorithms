"""Imports needed by class."""
from functools import reduce
from linked_list import LinkedList


class HashTable:
    """HashTable class."""


def __init__(self, max_size=1024):
        """Hash Table init."""
        self.max_size = max_size
        self.buckets = [LinkedList() for _ in range(max_size)]


def _hash_key(self, val):
        """Generate the hash key."""
        return sum(map(lambda x: ord(x), val)) % self.max_size


def set(self, key, val):
        """Insert val into hash table."""
        return self.buckets[self._hash_key(key)].insert({key: val})


def get(self, key):
        """Return the value associated with the given key."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            return self.buckets[self.hash_key(key)]


def remove(self, key, dump=False):
        """Remove bucket value."""
        bucket = self.buckets[self._hash_key(key)]
        current = bucket.head
        last = current
        while current:
            if key in current.val.keys():
                if dump:
                    bucket.head = None
                    bucket._size = 0
                else:
                    if last is not current:
                        last._next = current._next
                    else:
                        bucket.head = current._next
                return current.val[key]

            last = current
            current = current._next
