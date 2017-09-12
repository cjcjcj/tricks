import collections


def __islist(el):
    return isinstance(el, list)


def __isiterable(el):
    return isinstance(el, collections.Iterable)


def __reasonable(el):
    return isinstance(el, collections.Iterable) and \
           not isinstance(el, str) and \
           not isinstance(el, dict)


def nested_to_flat(l, predicate=__reasonable):
    for el in l:
        if predicate(el):
            yield from nested_to_flat(el, predicate=predicate)
        else:
            yield el


if __name__ == '__main__':
    l = [
        [ [1,2,3], 4, 5],
        [6,],
        7,
        '123',
        {'a': 0, None: False},
        (i for i in range(5))
    ]
    flat_l = list(nested_to_flat(l))
    # [1, 2, 3, 4, 5, 6, 7, '123', {'a': 0, None: False}, 0, 1, 2, 3, 4]
    print(flat_l)
