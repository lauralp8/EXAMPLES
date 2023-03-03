from multiprocessing import Process, Pipe
from time import sleep
from threading import Barrier, Thread
from random import randint


def worker(conn):
    print('Awake, waiting for data')
    data = conn.recv()  # guardamos en data lo que el proceso va a recibir
    sleep(1)            # espera a recibir la información
    data = data ** 2    # data va a devolver el cuadrado
    conn.send(data)     # enviamos data de nuevo al proceso


if __name__ == '__main__':
    # creamos el proceso
    print('Main - starting, creating the Pipe')
    main_connection, worker_connection = Pipe()     # creamos la conexión
    print('Main - setting up the process')
    p = Process(target=worker, args=(worker_connection,))
    print('Main - starting process')
    p.start()                   # iniciamos el proceso
    sleep(1)                    # espera (mientras la función se ejecuta)
    main_connection.send(3)     # mandamos a la función el dato
    result = main_connection.recv()     # metemos en el result el valor que vamos a recibir de la otra función
    print(result)               # imprimimos el resultado



