from .queue import Queue


def breadth_first_traversal(bst):
    """ define a function to treavers a BST using breadth first method """
    string = ""
    queue = Queue()
    root = self.root
    queue.enqueue(root)
    print(root.val)

    while len(queue.queue_list) > 0:
        node = queue.dequeue()
        if node.left is not None:
            queue.enqueue(node.left)
        print(node.left.val)
        if node.right is not None:
            queue.enqueue(node.right)
        print(node.right.val)
