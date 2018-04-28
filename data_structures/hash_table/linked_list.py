"""Imports."""
from node import Node


class LinkedList:
    """Class for new linked lists."""

    def __init__(self, iter=[]):
        """Initializer."""
        self.head = None
        self._len = 0

        for item in iter:
            self.head = self.insert(item)

    def __len__(self):
        """Return len of the corrent object."""
        return self._len

    def __str__(self):
        """Return all items from the LL."""
        lis = ''
        current = self.head
        while current:
            lis += str(current.val) + ' '
            current = current._next
        return lis

    def insert(self, val):
        """Add item to the LL."""
        node = Node(val, self.head)
        self.head = node
        self._len += 1
        return self.head

    def find(self, val):
        """Search for element and return True or false."""
        if self.head is None:
            return False
        elif self.head == val:
            return True
        else:
            current = self.head
        while current:
            if val == current:
                return True
            current = current._next
        return False

    def append(self, value):
        """Append value at the end of the list."""
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(value)

        self._len += 1

    def insert_before(self, value, newval):
        """Insert new node before correct."""
        if self.head is not None:
            current = self.head
            if self.head == value:
                self.head = Node(newval, self.head)
            while current._next:
                current = current._next
                if current.val == value:
                    nxt = current._next
                    current._next = Node(newval, nxt)
                    self._len += 1
                else:
                    return False
        else:
            self.head = Node(newval)
            self._len += 1
        return self.__str__

    def insert_after(self, value, newval):
        """Insert new node after correct."""
        print(str(self))
        if self.head is not None:
            current = self.head
            if self.head.val == value:
                self.head._next = Node(newval, current._next)
                return True
            while current._next:
                current = current._next
                if current.val == value:
                    nxt = current._next
                    current._next = Node(newval, nxt)
                    self._len += 1
                else:
                    return False
        else:
            self.head = Node(newval)
            self._len += 1
        return self.__str__
