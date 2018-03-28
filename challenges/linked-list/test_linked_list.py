
from linked_list import mergeLists

# @pytest.fixture
# def empty_linked_list():
#     return LL()


# @pytest.fixture
# def n_linked_list_list():
#     return LL([1, 2, 3])


def test_mergeLists_xempty(empty_ll, n_linked_ll):
    mergeLists(empty_ll, n_linked_ll)
    assert str(empty_ll) == str([1, 2, 3])


def test_mergeLists_yempty(empty_ll, n_linked_ll):
    mergeLists(n_linked_ll, empty_ll)
    assert str(n_linked_ll) == str([1, 2, 3])


def test_mergeLists_dif_len(linked_list_zip, n_linked_ll):
    mergeLists(linked_list_zip, n_linked_ll)
    assert str(linked_list_zip) == str([9, 1, 8, 2, 7, 3, 6])

#     @pytest.fixture
# def linked_list_zip():
#     return LL((9, 8, 7, 6))

# def test_mergeLists_empty():
#     return LL(xlist(1, 2, 3), ylist())

# def test_mergeLists_len():
#     return LL(xlist.len != ylist.len)
