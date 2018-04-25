from .towers_of_hanoi import towers_of_hanoi as th
from .towers_of_hanoi import steps
import pytest


def test_empty_th():
    """test if input empty"""
    assert th(0, '', '', '') is None


# def test_th_1():
#     """ verify works with one disk """
#     assert len(list(steps(3))) == 3

# def test_th_5():
#     """ verify works with one disk """
#     assert len(list(th(5))) == 5


# def test_th_11():
#     """ verify works with one disk """
#     assert len(list(th(11))) == 11
