from .stack import Stack


def multi_bracket_validation(input):
    """ test for matching brackets and return bool """
    if type(input) is str:
        open_b = '({]'
        closed_b = ')}]'
        compare = Stack()

        for brac in input:
            if brac in open_b:
                compare.push(brac)
            elif brac in closed_b:
                if compare.top is None:
                    return False
                if closed_b.index(brac) != open_b.index(compare.pop()):
                    return False
                return compare.top is None

    return False
