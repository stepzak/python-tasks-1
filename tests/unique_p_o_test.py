import pytest

from src.flatten import flatten
from src.unique_preserve_order import unique_preserve_order

def test_ok():
    obj = [1, 2, 4, 4, 3, 3, 0, 0, 2, 0]
    assert unique_preserve_order(obj)==[1, 2, 4, 3, 0]


def test_not_iterable():
    obj = 1234
    with pytest.raises(TypeError):
        flatten(obj)
