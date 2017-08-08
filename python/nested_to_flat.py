import itertools


l = [[1,2,3], [4], [5,6]]

#################### OK ####################
lf1 = list(itertools.chain.from_iterable(l))
# lf1 = list(itertools.chain(*l))

lf2 = list(el for row in l for el in row)

################# bad idea #################
from functools import reduce

lf3 = sum(l, [])

lf4 = reduce(lambda x, y: x+y, l, [])

lf5 = []
for sl in l:
    lf5.extend(sl)

lf6 = []
for sl in l:
    for el in sl:
        lf6.append(el)
