class Node:
    """Creates Nodes"""

    def __init__(self, val, next=None):
        """Initializer."""
        self.val = val
        self._next = next

    def __str__(self):
        """Represent String."""
        return str(self.val)


class LinkedList:
    """New linked lists Class."""

    def __init__(self, iter=[]):
        """Class Init."""
        self.head = None
        self._len = 0
        for item in iter:
            self.head = self.insert(item)

    def __len__(self):
        """Find length of the current object."""
        return self._len

    def __str__(self):
        """Return items from LL."""
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
        """Search for element and return Bool."""
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
        """Add value at the end of the LL."""
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(value)
        self._len += 1

    def insert_before(self, value, newval):
        """Insert new node before current."""
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
        """Insert new node after current."""
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

    def ll_kth_from_end(self, k):
        """Find node (k) from end."""
        if k < 0 or self._len - k < 0:
            return False
        size = len(self)
        index = size - k - 1
        if not (0 <= index < size):
            raise IndexError('LinkedList index out of bounds')
        node = self.head
        for _ in range(index):
            node = node._next
        return node

    def has_loop(self):
        """Will check for loop inside LL."""
        if self.head is None:
            return False
        if self.head._next is self.head:
            return True
        slow = self.head
        fast = self.head
        while fast is not None:
            slow = slow._next
            fast = fast._next._next
            if slow is fast:
                return True
            return False


def merge_lists(list1, list2):
    """Merge two LL."""
    if len(list1) == 0:
        return list2.head
    elif len(list2) == 0:
        return list1.head
    else:
        a = node = list1.head
        if not node:
            return list2.head
        b = list2.head
        while a and b:
            a._next, b = b, a._next
            a = a._next
        return node