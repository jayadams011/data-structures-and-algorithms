from queue_with_stacks import Queue as q
import pytest


@pytest.fixture
def empty_q():
    return q()


@pytest.fixture
def small_q():
    return q([1, 2, 3, 4])


def test_constructor(empty_q):
    """ test constructor """
    assert empty_q._len == 0

