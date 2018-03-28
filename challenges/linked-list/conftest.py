import pytest
from linked_list import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def n_linked_ll():
    return LL([1, 2, 3])


@pytest.fixture
def m_linked_ll():
    return LL([1, 'b', 2, 'd'])


@pytest.fixture
def linked_list_dict():
    return LL({'a': 1, 'b': 2, 'c': 3})


@pytest.fixture
def linked_list_tuple():
    return LL((1, 2, 3))


@pytest.fixture
def test_kthFromEnd_emp():
    return LL()


@pytest.fixture
def linked_list_zip():
    return LL((9, 8, 7, 6))
