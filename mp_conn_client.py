from multiprocessing.connection import Client
import time

Address = ('localhost', 6000)
with Client(Address, authkey=b'password') as conn:
    conn.send('foo')
    time.sleep(1)
    conn.send('close connection')
    conn.close()

time.sleep(1)

with Client(Address, authkey=b'password') as conn:
    conn.send('bar')
    conn.send('close server')
