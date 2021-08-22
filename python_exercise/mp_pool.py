from multiprocessing import Pool, TimeoutError, cpu_count
import time
import os


def f(x):
    return x*x


if __name__ == '__main__':
    print(os.cpu_count())
    print(cpu_count())
    with Pool(processes=4) as p:
        print(p.map(f, range(10)))
        for i in p.imap_unordered(f, range(10)):
            print(i)

        res = p.apply_async(f, (20,))
        print(res.get(timeout=1))

        res = p.apply_async(os.getpid, ())
        print(res.get(timeout=1))

        multiple_results = [p.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        res = p.apply_async(time.sleep, (5,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print('Timeout Error')

        print('pool available')

    print('pool closed')
