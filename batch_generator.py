from typing import Sequence


def batch_generator(obj: Sequence, batch_size: int):
    if batch_size<1:
        raise ValueError("batch_size must be more then 0")
    current_index = 0
    while current_index+batch_size<len(obj):
        yield tuple(obj[current_index:current_index + batch_size])
        current_index+=batch_size
    yield tuple(obj[current_index:])

if __name__ == "__main__":
    g = batch_generator([1, 2, 3, 4, 5, 6], 7)
    for i in g:
        print(i)


