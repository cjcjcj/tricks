# '1.2.3.4.5' -> ['1.2.3.4.5', '1.2.3.4', '1.2.3', '1.2', '1']

import itertools


def foo(s):
    s_s = s.split('.')
    return ('.'.join(s_s[:i]) for i in range(len(s_s), 0, -1))


def foo2(s):
    """author: @reverendhomer"""
    while s:
        yield s
        s, *_ = s.rpartition('.')


def foo3(s):
    join_2_strings = lambda x,y: '.'.join((x, y))
    return itertools.accumulate(s.split('.'), join_2_strings)


if __name__ == '__main__':
    s = '1.2.3.4.5'
    list(foo(s))
    list(foo2(s))
    list(foo3(s))