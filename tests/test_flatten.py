import pytest

from src.flatten import flatten

def test_ok():
    obj = [1, 2, [3, 4, [5, 6, [7, 8]], 9, 10]]
    assert flatten(obj)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_not_iterable():
    obj = 1234
    with pytest.raises(TypeError):
        flatten(obj)