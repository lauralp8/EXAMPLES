"""
 # PORQUE NO FUNCIONA ESTE

def print_it(msg:str, barrier: Barrier):
    t = rand(1,20)/10
    print(f'\nExecuting print {msg} with timer: {t}')
    for i in range(0,10):
        print(msg, end = '', flush=True)
        sleep(t)
    print(f'\nPrinting end: {msg}')
    barrier.wait()
    print(f'\nReturning from print_it: {msg}')

def main():
    print('Main - Starting')
    barrier = Barrier(3, callback)
    t1 = Thread(target = print_it, args = ('A', barrier))
    t2 = Thread(target=print_it, args=('A', barrier))
    t3 = Thread(target = print_it, args = ('A', barrier))
    t1.start()
    t2.start()
    t3.start()

"""
from time import sleep
from threading import Barrier, Thread
from random import randint


def print_it(msg: str, barrier: Barrier):
    print('print_it for:', msg)
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    sleep(randint(1, 6))
    print('Wait for barrier with:', msg)
    barrier.wait()
    print('Returning from print_it:', msg)


def callback():
    print('\nCallback Executing')


def main():
    print('Main - Starting')
    barrier = Barrier(3, callback)
    t1 = Thread(target=print_it, args=('A', barrier))
    t2 = Thread(target=print_it, args=('A', barrier))
    t3 = Thread(target=print_it, args=('A', barrier))
    t1.start()
    t2.start()
    t3.start()
    print('Main - Done')


if __name__ == '__main__':
    main()
