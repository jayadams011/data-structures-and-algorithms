
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


def test_empty_empty_queue(empty_qu):
    """test empty queue"""
    assert empty_qu.front is None
    assert empty_qu.back is None
    assert empty_qu._len == 0


def test_empty_empty_add(empty_qu):
    """test enqueue with empty"""
    empty_q.enqueue(2)
    assert empty_qu.front.val == 2
    assert empty_qu._len == 1
    assert empty_qu.back.val == 2


def test_small_len(small_qu, empty_qu):
    """test len method """
    assert small_qu._len == 4
    assert empty_qu._len == 0


def test_small_str(small_qu):
    """test str repr"""
    assert str(small_qu) == '1 2 4 5'


def test_small_enquue(small_qu):
    """test front and back"""
    small_q.enqueue(3)
    assert small_qu.front.val == 1
    assert small_qu.back.val == 3
