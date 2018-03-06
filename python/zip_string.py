from itertools import chain


def __zip_str_g(instr):
    l, li = instr[0], 0
    for c in instr:
        if l != c:
            yield l, li > 1 and str(li) or None
            l, li = c, 0
        li += 1
    yield l, li > 1 and str(li) or None


def zip_str(instr):
    if not instr:
        return ''
    zipped = chain.from_iterable(__zip_str_g(instr))
    without_zeroes = filter(None, zipped)
    return ''.join(without_zeroes)
