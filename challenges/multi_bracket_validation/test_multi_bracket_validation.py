from .multi_bracket_validation import multi_bracket_validation as mbv
import pytest


def test__empty_exp():
    """test if input is not a string"""
    assert mbv('') is False
