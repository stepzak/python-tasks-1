from typing import Iterable, Any


def is_flat(x: Any) -> bool:
    return isinstance(x, str) or not isinstance(x, Iterable)

def flatten(nested: Iterable) -> Iterable:
    ret = []
    stack_to_append = []
    for val in nested:


        if not is_flat(val):
            stack_to_append.append(val)
            ind = 0
            while True:

                c = stack_to_append[-1]
                for x in range(len(c)):

                    if is_flat(c[x]):
                        stack_to_append.insert(ind, c[x])

                        ind += 1
                    else:
                        stack_to_append[-1] = stack_to_append[-1][x+1:]
                        stack_to_append.append(c[x])
                        break
                else:
                    stack_to_append.pop()
                    to_check = [is_flat(x) for x in stack_to_append]
                    if all(to_check):
                        break
                    continue

                to_check = [is_flat(x) for x in stack_to_append]
                if all(to_check):
                    break
            ret.extend(stack_to_append)
            stack_to_append = []
            continue

        ret.append(val)
    return type(nested)(ret)

if __name__ == "__main__":
    print(flatten([1, 2, [3, 4, [5, 6, (7, 8)]], [9, 10, (11, 12), 13, 14]]))