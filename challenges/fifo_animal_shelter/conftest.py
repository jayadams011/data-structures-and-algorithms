import pytest
from fifo_animal_shelter import AnimalShelter as AS


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def n_linked_ll():
    return LL([1, 2, 3])


@pytest.fixture
def has_loop_ll():
    ll_loop = LL([1, 2, 3, 4, 5])
    ll_loop.head._next._next._next._next._next = ll_loop.head._next._next
    return ll_loop


@pytest.fixture
def m_linked_ll():
    return LL([1, 'b', 2, 'd'])


@pytest.fixture
def linked_list_dict():
    return LL({'a': 1, 'b': 2, 'c': 3})
