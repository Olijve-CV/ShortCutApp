import gevent
from gevent.lock import Semaphore

sem = Semaphore(1)

def f1():
    for i in range(5):
        sem.acquire()
        print('1 this is ' + str(i))
        gevent.sleep(2)
        sem.release()


def f2():
    for i in range(5):
        sem.acquire()
        print('2 that is ' + str(i))
        gevent.sleep(2)
        sem.release()


t1 = gevent.spawn(f1)
t2 = gevent.spawn(f2)
gevent.joinall([t1, t2])
from functools import wraps