"""Node."""


class Node:
    """Node."""

    def __init__(self, val, next=None):
        """Init function."""
        self.val = val
        self._next = next

    def __str__(self):
        """Str representation."""
        return str(self.val)
