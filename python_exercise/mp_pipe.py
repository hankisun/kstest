from multiprocessing import Process, Pipe
import os
import time


def f(conn):
    print(__name__)
    print('pid: ', os.getpid())
    print('ppid: ', os.getppid())
    while True:
        msg = conn.recv()
        print(msg)
        if msg == 'close':
            break
        conn.send(['hello'])

    conn.close()


if __name__ == '__main__':
    print(__name__)
    print(os.cpu_count())
    print('pid: ', os.getpid())

    parent_conn, child_conn = Pipe()
    p = Process(target=f, name='child_process',
                args=(child_conn,), daemon=True)
    p.start()
    print('child pid ', p.pid, p.name)
    parent_conn.send(['Im parent'])
    print(parent_conn.recv())
    print('exit code : ', p.exitcode)
    print('is alive {}'.format(p.is_alive()))

    parent_conn.send('This is second turn')
    print(parent_conn.recv())
    # p.join()
    # print('is alive {}'.format(p.is_alive()))
    print('exit code : ', p.exitcode)
    print('is alive {}'.format(p.is_alive()))

    parent_conn.send('close')

    # time.sleep(4)
    print('exit code : ', p.exitcode)
    time.sleep(1)
    print('is alive {}'.format(p.is_alive()))
