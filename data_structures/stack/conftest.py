import pytest
from .stack import Stack


@pytest.fixture
def empty_stack():
    x = Stack()
    return x


@pytest.fixture
def small_stack():
    return Stack([1, 2, 3, 4])
