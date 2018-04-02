import pytest
from .queue import Queue


@pytest.fixture
def empty_qu():
    x = Queue()
    return x


@pytest.fixture
def small_qu():
    return Queue([1, 2, 3, 4])
