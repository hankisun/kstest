from multiprocessing import Process
import os


class args:
    d = {'a': 1, 'b': [1, 2, 3]}


def info(title):
    print(title)
    print('module_name: ', __name__)
    print('parent pid: ', os.getppid())
    print('pid: ', os.getpid())


def f(name, num, args):
    # info('function f')
    print(f'hello {name}, num {num}')
    if num == 2:
        args.d['b'][2] = 23
    print(args.d)


if __name__ == '__main__':
    info('main line')
    # d = {'a': 1, 'b': [1, 2, 3]}
    for i in range(5):
        p = Process(target=f, args=('han', i, args))
        p.start()
        p.join()
        print(args.d)

    args.d['b'][2] = 13
    print(args.d)
    print('end of main')
