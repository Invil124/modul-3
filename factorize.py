from time import time
from multiprocessing import Pool, cpu_count


def factorize(*number):
    a = []
    b = []
    c = []
    d = []

    for i in range(1, number[0] + 1):
        if number[0] % i  == 0:
            a.append(i)

    for i in range(1, number[1] + 1):
        if number[1] % i  == 0:
            b.append(i)

    for i in range(1, number[2] + 1):
        if number[2] % i  == 0:
            c.append(i)

    for i in range(1 , number[3] + 1):
        if number[3] % i  == 0:
            d.append(i)




    return a,b,c,d


if __name__ == '__main__':

    t1 = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(a)
    print(b)
    print(c)
    print(d)
    print(f'Time in one stream: {time() - t1}. Result ')


    t2 = time()
    processors = cpu_count()
    pool = Pool(processors)
    result = pool.apply_async(factorize, (128, 255, 99999, 10651060))
    print(f'Multiprocessor time:  {time() - t2}. Result {result.get()}')
