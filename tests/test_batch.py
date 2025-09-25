import pytest
from src.batch_generator import batch_generator

def test_arr():
    arg = [1, 2, 3, 4]
    batch_size = 2
    gen = batch_generator(arg, batch_size)
    assert next(gen) == (1, 2)
    assert next(gen) == (3, 4)
    try:
        next(gen)
        assert False
    except StopIteration:
        assert True

def test_tuple():
    arg = (1, 2, 3, 4)
    batch_size = 3
    gen = batch_generator(arg, batch_size)
    assert next(gen) == (1, 2, 3)
    assert next(gen) == (4,)
    try:
        next(gen)
        assert False
    except StopIteration:
        assert True

def test_value_error_negative():
    arg = (1, 2, 3, 4)
    batch_size = -1

    with pytest.raises(ValueError):
        gen = batch_generator(arg, batch_size)
        next(gen)

def test_float_batch_size():
    arg = (1, 2, 3, 4)
    batch_size = 1.5

    with pytest.raises(TypeError):
        gen = batch_generator(arg, batch_size)
        next(gen)

def test_str_batch_size():
    arg = (1, 2, 3, 4)
    batch_size = "1"

    with pytest.raises(TypeError):
        gen = batch_generator(arg, batch_size)
        next(gen)

def test_not_sequence():
    arg = 123
    batch_size = 2

    with pytest.raises(TypeError):
        gen = batch_generator(arg, batch_size)
        next(gen)