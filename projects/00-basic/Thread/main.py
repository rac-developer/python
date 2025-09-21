
import threading
import time

print(threading.active_count())
# 1

# El hilo que se encarga de ejecutar nuestro programa
print(threading.enumerate())
# [<_MainThread(MainThread, started 22000)>]

def desayunar():
  print('Iniciando desayuno')
  # .sleep es un temporizador en segundos
  time.sleep(5)
  print('Terminado desayuno')

def tomar_cafe():
  print('Iniciando cafe')
  time.sleep(7)
  print('Terminado cafe')

def estudiar():
  print('Iniciando estudio')
  time.sleep(10)
  print('Terminado estudio')
  
# .perf_counter estamos iniciando un cronometro
inicio = time.perf_counter()  

# Esto ejecuta las 3 funciones al mismo tiempo

x = threading.Thread(target=desayunar, args=())
x.start()

y = threading.Thread(target=tomar_cafe, args=())
y.start()

z = threading.Thread(target=estudiar, args=())
z.start()

# .join Ejecuta todo al mismo tiempo

x.join()
y.join()
z.join()

fin = time.perf_counter()
tiempo = fin - inicio

print(tiempo)