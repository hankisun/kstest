from multiprocessing import Process, Pipe
import os
import time


def cal(n):
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret


def f(conn):
    print(__name__)
    print('pid: ', os.getpid())
    print('ppid: ', os.getppid())

    while True:
        msg = conn.recv()
        print(msg)
        if msg == 'close':
            break

        conn.send(cal(msg))

    conn.close()


if __name__ == '__main__':
    print(__name__)
    print(os.cpu_count())
    print('pid: ', os.getpid())

    start = time.time()
    parent1_conn, child1_conn = Pipe()
    p = Process(target=f, name='child_process',
                args=(child1_conn,), daemon=True)
    p.start()

    parent2_conn, child2_conn = Pipe()
    p2 = Process(target=f, name='child_process',
                 args=(child2_conn,), daemon=True)
    p2.start()

    print('child pid ', p.pid, p.name)
    parent1_conn.send(100000000)

    print('child pid ', p2.pid, p2.name)
    parent2_conn.send(100000000)

    print(parent1_conn.recv())
    print(parent2_conn.recv())

    parent1_conn.send('close')
    parent2_conn.send('close')
    print('elapsed {}'.format(time.time() - start))
