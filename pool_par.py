from functools import reduce
from multiprocessing import cpu_count, Pool
import time
start_time = time.time()


def square(n):
    return n*n


if __name__ == '__main__':
    print("Number of cores avaibles equals %s" % cpu_count())

    # create a pool of workes
    with Pool() as pool:
        # create an array of 5000 intigers
        r = range(1, 5000)
        result = pool.map(square, r)
    total = reduce(lambda x, y: x + y, result)

    print("The sum oh the squre of the first 5000 integers is %s" % total)

    print("\n----- %s seconds ---" % (time.time() - start_time))
