from typing import Sequence

def batch_generator(obj: Sequence, batch_size: int):

    if not isinstance(obj, Sequence):
        raise TypeError("obj must be a sequence")

    if not isinstance(batch_size, int):
        raise TypeError("batch_size must be an integer")
    if batch_size<1:
        raise ValueError("batch_size must be more then 0")
    if float(batch_size) != int(batch_size):
        raise TypeError('batch_size must be an integer')


    current_index = 0
    while current_index+batch_size<len(obj):
        yield tuple(obj[current_index:current_index + batch_size])
        current_index+=batch_size
    yield tuple(obj[current_index:])

if __name__ == "__main__":
    g = batch_generator([1, 2, 3, 4, 5, 6], 2)
    for i in g:
        print(i)


