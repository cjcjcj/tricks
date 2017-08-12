# it can be dangerous if generator has infinite loop

def generator(n):
    yield from range(n)


def generator_len(gen):
    return sum(1 for _ in gen)


# O(1) for iterable types w/ length specified
def iterable_len(iterable):
    try:
        return len(iterable)
    except TypeError:
        return sum(1 for _ in iterable)


if __name__ == '__main__':
    my_gen = generator(10)
    print(generator_len(my_gen))
    my_iterable = list(generator(10))
    print(iterable_len(my_iterable))