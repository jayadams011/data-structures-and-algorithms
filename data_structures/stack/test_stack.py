from .stack import Stack
import pytest


def test_push_empty_stack(empty_stack):
    """ to test push if stack is empty """
    assert empty_stack.top is None


def test_push_add_val(empty_stack):
    """ to test if push adds 5 """
    empty_stack.push(5)
    assert empty_stack.top.val == 5


def test_small_len(small_st, empty_st):
    """test len prebuid list"""
    assert len(small_st) == 4
    assert len(empty_st) == 0


def test_push_add_multi_val(empty_stack):
    """ test push 3 times """
    empty_stack.push(5)
    empty_stack.push(6)
    empty_stack.push(9)
    assert empty_stack.top.val == 9
    assert empty_stack.top._next.val == 6


def test_small_push(small_st):
    """test push method"""
    small_st.push(2)
    small_st.push(4)
    assert len(small_st)


def test_pop_take_val(empty_stack):
    """ raise error if stack is empty before pop """
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_small_pop(small_st):
    """test pop method"""
    current = small_st.top
    assert small_st.pop() is current
    assert len(small_st) == 3


def test_peek_val_empty(small_stack, empty_stack):
    """ see if peek sees top and if len is 0 """
    assert small_stack.peek() == small_stack.top
    assert len(small_stack) == 0
