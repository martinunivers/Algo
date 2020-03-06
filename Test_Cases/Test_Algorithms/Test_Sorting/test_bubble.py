# test_bubble.py
# from Algo.Algorithms.Sorting import bubble
from Algorithms.Sorting import bubble


def test_bubble01():
    assert bubble.bubble([4, 3, 3, 0], "ASC") == [0, 3, 3, 4]


def test_bubble02():
    assert bubble.bubble([4], "ASC") == [4]


def test_bubble03():
    assert bubble.bubble([], "ASC") == []


def test_bubble04():
    assert bubble.bubble([4, 3, 0, 3], "DESC") == [4, 3, 3, 0]