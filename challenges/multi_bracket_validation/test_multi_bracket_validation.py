from .multi_bracket_validation import multi_bracket_validation as mbv
import pytest


def test_empty_exp():
    """test if input is not a string"""
    assert mbv('') is True


def test_match_input():
    """test correct input"""
    assert mbv('[[][]]') is False


def test_not_match_input():
    """test not match input"""
    assert mbv('{{[}}') is True


def test_wrong_input():
    """test input is not a string"""
    assert mbv([1, 2, 3, 4]) is False
