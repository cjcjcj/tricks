from itertools import tee, zip_longest


def pairwise_gen_longest(iterable):
    a, b = tee(iterable)
    next(b)
    return zip_longest(a, b)


def pairwise_gen(iterable):
    a, b = tee(iterable)
    next(b)
    return zip(a, b)


if __name__ == '__main__':
    l = list(range(5))
    pairwise_longest = list(pairwise_gen_longest(l))
    pairwise = list(pairwise_gen(l))
    # [(0, 1), (1, 2), (2, 3), (3, 4), (4, None)]
    print(pairwise_longest)
    # [(0, 1), (1, 2), (2, 3), (3, 4)]
    print(pairwise)
