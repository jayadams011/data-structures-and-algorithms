"""Imports."""
from hash_table import HashTable


def tree_intersection(tree1, tree2):
    """Func takes 2 bt as an arg and returns a set of the intersection."""
    if tree1.root is None or tree2.root is None:
        return False
    table = HashTable()
    tree1.in_order(table.set)
    arr = []

    def check(value):
        number = table.hash_key(str(value))
        if type(table.buckets[number]) == dict:
            arr.append(value)
    tree2.in_order(check)
    return arr
