# test_bubble.py
import pytest
#from Algo.Algorithms.Sorting import bubble
from Algorithms.Sorting import bubble

def test_bubble():
    assert bubble.bubble([4, 3, 1, 0], "ASC") == [0, 1, 3, 4]
