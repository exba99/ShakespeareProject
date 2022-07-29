
from functools import reduce


def counter():
    print(reduce(lambda x, y: x+y, list(map(lambda n: n * n, range(1, 5001)))))


def test():
    print(lambda: 1)


if __name__ == '__main__':
    # counter()
    test()
