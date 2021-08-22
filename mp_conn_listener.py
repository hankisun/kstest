from multiprocessing.connection import Listener

Address = ('localhost', 6000)

with Listener(Address, authkey=b'password') as l:
    running = True
    while running:
        conn = l.accept()
        print('connection accepted from ', l.last_accepted)
        while True:
            msg = conn.recv()
            print(msg)
            if msg == 'close connection':
                conn.close()
                break
            if msg == 'close server':
                conn.close()
                running = False
                break
