from multiprocessing import Process, Lock
import os


def func(lock, num):
    lock.acquire()
    try:
        print("Hello {} mypid is {}".format(num, os.getpid()))
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=func, args=(lock, i))
        p.start()

    print('end of main')
