import threading
import time

def tarea_hilo(numero):
    for i in range(5):
        print(f'Hilo {numero}: Ejecutando tarea {i + 1}')
        time.sleep(1)

hilo1 = threading.Thread(target=tarea_hilo, args=(1,))
hilo2 = threading.Thread(target=tarea_hilo, args=(2,))
hilo3 = threading.Thread(target=tarea_hilo, args=(3,))

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

print('Todas las tareas han sido completadas.')
