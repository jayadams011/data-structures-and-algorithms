
def towers_of_hanoi(n, peg_1, peg_3, peg_2):
    if n == 0:
        towers_of_hanoi(n-1, peg_1, peg_2, peg_3)
        steps(peg_1, peg_3)
        towers_of_hanoi(n-1, peg_2, peg_3, peg_1)


def steps(fp, tp):
    print("moving disk from", fp, "to", tp)
    return("moving disk from", fp, "to", tp)

towers_of_hanoi(3, "A", "B", "C")
