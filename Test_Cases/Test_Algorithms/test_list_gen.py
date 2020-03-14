# test_list_gen.py
"""
Test list_gen.py module using pytest
"""

from Algorithms import  list_gen
import random


def test_unsorted_list01():
    random.seed(1)
    assert list_gen.unsorted_list(0, 5, 5) == [1, 4, 0, 2, 0]


def test_unsorted_list02():
    random.seed(1)
    assert list_gen.unsorted_list(5, 0, 5) == []


def test_unsorted_list03():
    random.seed(1)
    assert list_gen.unsorted_list(0, 5, 0) == []


def test_sorted_list01():
    random.seed(1)
    assert list_gen.sorted_list(0, 5, 10) == [1, 6, 7, 10, 11, 15, 19, 23, 29, 33]


def test_sorted_list02():
    random.seed(1)
    assert list_gen.sorted_list(5, 0, 10) == []


def test_sorted_list03():
    random.seed(1)
    assert list_gen.sorted_list(0, 5, 0) == []


def test_string_pattern01():
    assert list_gen.string_pattern("A", 5) == "AAAAA"
    

def test_string_pattern02():
    assert list_gen.string_pattern(1, 5) == "11111"


def test_string_pattern03():
    assert list_gen.string_pattern("", 5) == ""

test_unsorted_list03()