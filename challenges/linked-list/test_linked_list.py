import pytest
from ll_insertions import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])
