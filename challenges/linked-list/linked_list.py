from node import Node


class LinkedList:
    """ class for new linked list """
    def __init__(self, iter=[]):
        self.head = None
        self._len = 0

        for item in iter:
            self.head = Node(item, self.head)
            self._len += 1

    def __len__(self):
        """ return len of the current object """
        return self._len

    def __str__(self):
        """ return all items from the LL """
        lis = []
        current = self.head
        for _ in range(self._len+1):
            lis.append(current)
            current = current._next
        return str(lis)

    def insert(self, val):
        """ add item to LL """
        self.head = Node(val, self.head)
        self._len += 1

    def find(self, val):
        """ search for element and return TRUE or False"""
        x = self.head
        while x is not None:
            if x == val:
                return True
            return False

    def append(self, value):
        """ append vlue at the end of the lsit """
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(value)

    def insert_before(self, val, newVal):
        """ insert new node before current """
        if self._size == 0:
            return 'Linked List is Empty'
        previous_node = self.head
        self.head = Node(newVal, previous_node)
        return self
        if previous_node._next:
            x = previous_node._next
            while x:
                if x.val == val:
                    print('x', x)
                    new_insert = Node(newVal, x)
                    previous_node._next = new_insert
                    self._size += 1
                    print('length => {}'.format(self.__len__()))
                    return self
                previous_node = x
                x = x._next
        return 'did not insert'

    def insert_after(self, val, newVal):
        """ Insert new node after current """
        if self._size == 0:
            return 'Linked List is Empty'
        node = self.head
        while node:
            if node.val == val:
                print('Node.val => {}'.format(node.val))
                newNode = Node(newVal, node._next)
                node._next = newNode
                self._size += 1
                return
            node = node._next
        return 'did not insert'

        def kthFromEnd(self, k):
            """ find node (k) from end """
            x = self._size - (k-1)
            node = self.head
            counter = 0 
            while node:
                if counter == x:
                    return node
                counter += 1
                node = node._next
            raise IndexError('Requested node outside link list length')
            