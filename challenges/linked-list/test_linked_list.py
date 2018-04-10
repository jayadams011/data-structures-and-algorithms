
from linked_list import mergeLists


def test_mergeLists_xempty(empty_ll, n_linked_ll):
    """test for merging with empty list as first list """
    mergeLists(empty_ll, n_linked_ll)
    assert str(empty_ll) == str([1, 2, 3])


def test_mergeLists_yempty(empty_ll, n_linked_ll):
    """test for merging with empty list as second list """
    mergeLists(n_linked_ll, empty_ll)
    assert str(n_linked_ll) == str([1, 2, 3])


def test_mergeLists_dif_len(linked_list_zip, n_linked_ll):
    """ test for merge like zip """
    mergeLists(linked_list_zip, n_linked_ll)
    assert str(linked_list_zip) == str([9, 1, 8, 2, 7, 3, 6])


def test_ll_loop(has_loop_ll):
    """ test LL has a loop """
    assert has_loop_ll.hasLoop() is True


def test_ll_loop_f(n_linked_ll):
    """ test is doesnt have a loop """
    assert n_linked_ll.hasLoop() is False


def test_ll_loop_e(empty_ll):
    """ test if empty ll has a loop """
    assert empty_ll.hasLoop() is False


# def test_ll.insert_before(linked_list_insert):
#     """ test if insert a 1 works """
#     ll.insert_before(2, 10)
#     assert linked_list_insert == '1102'


    # # ll.insert(1)
    # ll.insert(3)
    # ll.insert(6)
    # ll.insert(9)
    # print(ll.head.val)
    # print(ll.__str__())
    # ll.insert_before(6, 8)
    # ll.insert_after(3, 5)
    # print(ll.__str__())
