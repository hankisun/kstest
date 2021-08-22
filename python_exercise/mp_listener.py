from multiprocessing.connection import Listener, Client
from multiprocessing import Process
from array import array

Address = ('localhost', 6000)


def listener():
    with Listener(Address, authkey=b'password') as l:
        with l.accept() as conn:
            print('connection from ', l.last_accepted)
            conn.send([2.25, None, 'junk', float])
            conn.send_bytes(b'hello')
            conn.send_bytes(array('i', [42, 1729]))


if __name__ == '__main__':
    p = Process(target=listener, name='listener')
    p.start()
    print('child proces: ', p.pid, p.name)

    with Client(Address, authkey=b'password') as conn:
        print(conn.recv())
        print(conn.recv_bytes())
        arr = array('i', [0, 0, 0, 0, 0])
        print(conn.recv_bytes_into(arr))
        print(arr)
    print('exit code : ', p.exitcode)
    p.join()
    print('exit code : ', p.exitcode)
