from queue import Queue


def find_matches(self, func, val):
    '''Perform func on each node breadth first'''
    def recurse(nodelist):
        new_list = []
        for node in nodelist:
            func(node)
            for child in node.children:
                if child.val == val
                new_list.append(child)

        if len(new_list):
            recurse(new_list)

    if self.root:
        recurse([self.root])
    return new_list
