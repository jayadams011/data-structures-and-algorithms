
def test_enqueue(empty_qu):
    """ test if empty add """
    empty_qu.enqueue(1)
    assert empty_qu.back.val == 1


def test_enqueue_1(small_qu):
    """ test if it finds value """
    small_qu.enqueue(3)
    assert small_qu.front.val == 1
    assert small_qu.back.val == 3


def test_enqueue_2(small_qu):
    """ test if it will add two values """
    small_qu.enqueue(10)
    small_qu.enqueue(5)
    assert small_qu.front.val == 1
    assert small_qu.back.val == 5


def test_emp_enqueue(empty_qu):
    """ testing if it adds to an empty qu """
    empty_qu.enqueue(10)
    empty_qu.enqueue(5)
    assert empty_qu.front.val == 10
    assert empty_qu.back.val == 5
