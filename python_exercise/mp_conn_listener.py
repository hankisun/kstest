from multiprocessing.connection import Listener
import time
import os

Address = ('localhost', 6000)

with Listener(Address, authkey=b'password') as l:
    running = True
    print(f'start listener... pid {os.getpid()}')
    while running:
        conn = l.accept()
        print('connection accepted from ', l.last_accepted)
        while True:
            try:
                msg = conn.recv()
            except ConnectionAbortedError as e:
                print(e)
                break
            except ConnectionResetError as e:
                print(e)
                break

            print(msg)
            time.sleep(5)
            if msg == 'close connection':
                conn.close()
                break
            if msg == 'close server':
                conn.close()
                running = False
                print('close listener...')
                break
            if msg == 'hello':
                ret = 'hello client. listener is running'
            else:
                ret = {'code': 0, 'msg': f'success {l.address}'}

            conn.send(ret)
