from typing import Iterable

def unique_preserve_order(obj: Iterable):
    if not isinstance(obj, Iterable):
        raise TypeError("obj must be iterable")

    ret = []
    for x in obj:
        if x not in ret:
            ret.append(x)
    return type(obj)(ret)

if __name__ == "__main__":
    print(unique_preserve_order((1, 3, 2, 1, 5, 2, 4)))