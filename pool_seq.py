from functools import reduce
import time
start_time = time.time()

if __name__ == '__main__':
    r = range(1, 5000)
    result = map(lambda x: x * x, r)
    total = reduce(lambda x, y: x + y, result)
    print("The sum oh the squre of the first 5000 integers is %s" % total)
    print("\n----- %s seconds ---" % (time.time() - start_time))
