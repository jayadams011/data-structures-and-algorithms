from .bst import BST
import pytest


@pytest.fixture
def new_bst():
    return BST()


@pytest.fixture
def filled_bst():
    return BST([4, 3, 2, 1, 8, 6, 12, 9])
