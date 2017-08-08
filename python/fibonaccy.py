def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib_seq = list(fib(5))
    print(fib_seq)
