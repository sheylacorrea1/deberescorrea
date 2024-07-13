import threading
import time

# Creamos un evento
evento = threading.Event()

# Función que espera a que el evento se active y luego imprime un mensaje
def espera_evento():
    print("Hilo esperando evento")
    # Esperamos a que el evento se active
    evento.wait()
    print("Evento ha sido activado")

# Función que activa el evento después de un cierto tiempo
def activar_evento():
    print("Hilo activando evento")
    # Esperamos un poco antes de activar el evento
    time.sleep(2)
    evento.set()
    print("Evento ha sido activado")

# Creamos dos hilos que ejecutarán las funciones
hilo1 = threading.Thread(target=espera_evento)
hilo2 = threading.Thread(target=activar_evento)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Programa terminado")