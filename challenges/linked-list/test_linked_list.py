
from linked_list import mergeLists


def test_mergeLists_xempty(empty_ll, n_linked_ll):
    mergeLists(empty_ll, n_linked_ll)
    assert str(empty_ll) == str([1, 2, 3])


def test_mergeLists_yempty(empty_ll, n_linked_ll):
    mergeLists(n_linked_ll, empty_ll)
    assert str(n_linked_ll) == str([1, 2, 3])


def test_mergeLists_dif_len(linked_list_zip, n_linked_ll):
    mergeLists(linked_list_zip, n_linked_ll)
    assert str(linked_list_zip) == str([9, 1, 8, 2, 7, 3, 6])


def test_ll_loop(has_loop_ll):
    assert has_loop_ll.hasLoop() is True


def test_ll_loop_f(n_linked_ll):
    assert n_linked_ll.hasLoop() is False


def test_ll_loop_e(empty_ll):
    assert empty_ll.hasLoop() is False
