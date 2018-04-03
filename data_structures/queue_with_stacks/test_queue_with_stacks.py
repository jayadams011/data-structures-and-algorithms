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
