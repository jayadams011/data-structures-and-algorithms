def breadth_first_traversal(self, func):
    '''Perform func on each node breadth first'''
    def recurse(nodelist):
        new_list = []
        for node in nodelist:
            func(node)
            for child in node.children:
                new_list.append(child)

        if len(new_list):
            recurse(new_list)

    if self.root:
        recurse([self.root])
