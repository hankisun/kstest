from multiprocessing.connection import Client
import time

Address = ('localhost', 6000)
with Client(Address, authkey=b'password') as conn:
    conn.send('foo')
    ret = conn.recv()
    print(ret)
    conn.send('close connection')
    conn.close()

time.sleep(1)

with Client(Address, authkey=b'password') as conn:
    conn.send('bar')
    ret = conn.recv()
    print(ret)
    conn.send('close server')
    conn.close()
