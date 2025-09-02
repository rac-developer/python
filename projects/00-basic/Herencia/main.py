from animal import Animal

class Perro(Animal):
    def ladrar(self):
        print("El perro esta ladrando")

class Gato(Animal):
    def maullar(self):
        print("El gato esta maullando")

perro = Perro()
gato = Gato()

print(perro.vivo)
# True
perro.comer()
# El animal esta comiendo
gato.dormir()
# El animal esta durmiendo

gato.maullar()
# El gato esta maullando
perro.ladrar()
# El perro esta ladrando

# # Anulacion de metodos
# class Animal:
#     def comer(self):
#         print("El animal esta comiendo")
        
# class Conejo(Animal):
#     def comer(self):
#         print("El conejo esta comiendo zanahorias")
        
# conejo =  Conejo()

# conejo.comer()
# # El conejo esta comiendo zanahorias

# # Herecia Multinivel
# class Organismo:
#     vivo = True
    
# class Animal(Organismo):
#     def comer(self):
#         print("El animal esta comiendo")
        
# class Perro(Animal):
#     def ladrar(self):
#         print("El perro esta ladrando")
        
# perro = Perro()

# perro.ladrar()
# # El perro esta ladrando
# print(perro.vivo)
# # True

# Herencia Multiple

class Presa:
    def huir(self):
        print("La presa esta huyendo")

class Depredador:
    def cazar(self):
        print("El depredador esta cazando")
        
class Conejo(Presa):
    pass

class Alcon(Depredador):
    pass

class Pez(Depredador, Presa):
    pass

conejo = Conejo()
halcon = Alcon()
pez = Pez()

conejo.huir()
# La presa esta huyendo

Alcon.cazar()
# El depredador esta cazando

pez.cazar()
# El depredador esta cazando

pez.huir()
# La presa esta huyendo