from multiprocessing.connection import Client
import time

Address = ('localhost', 6000)
with Client(Address, authkey=b'password') as conn:
    conn.send('foo2')
    ret = conn.recv()
    print(ret)
    conn.send('hello')
    ret = conn.recv()
    print(ret)
    conn.send('close connection')
    ret = conn.recv()
    print(ret)
    # conn.close()
