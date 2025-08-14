
from car import Car

auto1 = Car('Ford','mustang',1969, 'black')
auto2 = Car('Chevy','Corvette',2025, 'blue')

print(auto1.marca)
# Ford
print(auto2.marca)
# Chevy

auto1.encedido()
# El auto esta encedido!
auto2.apagado()
# El auto esta apagado!