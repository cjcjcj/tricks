def nested_to_flat(l):
    for el in l:
        if type(el) == type([]):
            yield from nested_to_flat(el)
        else:
            yield el


if __name__ == '__main__':
    l = [[[1,2,3],4,5],[6,],7]
    flat_l = list(nested_to_flat(l))
    # [1, 2, 3, 4, 5, 6, 7]
    print(flat_l)
