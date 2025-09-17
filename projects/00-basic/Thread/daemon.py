
import threading
import time

def tiempo():
  print()
  print()
  contador = 0
  while True:
    time.sleep(1)
    contador += 1
    print(contador, "Segundos")

# daemon cierra el programa automaticamente
x = threading.Thread(target=tiempo, daemon=True)

# .setDaemon es lo mismo que parametro daemon
# x.setDaemon(True)
x.start()

print(x.isDaemon())

entrada = input('Deseas salir?')