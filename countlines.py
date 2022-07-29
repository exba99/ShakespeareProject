# exercise here
import sys
from functools import reduce


def counter():
    print(list(zip(sys.argv[1:], map(count_lines_in_file, sys.argv[1:]))))
    print("The total number of lines is {}".format(total_lines()))


def count_lines_in_file(filename):
    """
    Counts the number of lines in a file.
    """
    try:
        with open(filename) as f:
            return len(f.readlines())
    except FileNotFoundError:
        print("File is not exist!")
        return -1


def total_lines():
    """
    Counts the number of lines in all files.
    """
    return reduce(lambda x, y: x + y, list(map(count_lines_in_file,  sys.argv[1:])))


if __name__ == '__main__':
    counter()
