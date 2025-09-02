
from car import Car

auto1 = Car('Ford','mustang',1969, 'black')
auto2 = Car('Chevy','Corvette',2025, 'blue')

auto2.ruedas = 2

print(auto1.ruedas)
# Ford
print(auto2.marca)
print(auto2.ruedas)
# Chevy

auto1.encedido()
# El auto esta encedido!
auto2.apagado()
# El auto esta apagado!