from .queue_with_stacks import Queue as z
import pytest


@pytest.fixture
def empty_q():
    return z()


@pytest.fixture
def small_q():
    return z([1, 2, 3, 4])


@pytest.fixture
def small_z():
    return z([])


def test_constructor(empty_q):
    """ test constructor """
    assert empty_q._len == 0


def test_enqueue(empty_q, small_q):
    """test enqueu on small and empty queue"""
    assert empty_q.enqueue(1) == empty_q.stack1
    assert empty_q.enqueue(10) == empty_q.stack1


def test_dequeue(empty_q):
    """test dequeue method"""
    empty_q.enqueue(1)
    assert empty_q.dequeue() == 1


def test_enqueue_val(empty_q, small_q):
    """test dequeu method for val"""
    empty_q.enqueue(5)
    small_q.enqueue(25)
    assert empty_q.stack1.top.val == 5
    assert small_q.stack1.top.val == 25


def test_dequeu_(small_q):
    """test dequeue from small q"""
    assert small_q.dequeue() == 2


def test_enqueue_and_dequeue(empty_q):
    """test empty q"""
    empty_q.enqueue(4)
    assert empty_q.dequeue() == 4
