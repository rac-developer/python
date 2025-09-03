
class Pato:
    def caminar(self):
        print("El pato esta caminando")
    def hablar(self):
        print("El pato esta haciendo cuac cuac")
        
class Perro:
    def caminar(self):
        print("El perro esta caminando")
    def hablar(self):
        print("El perro esta haciendo guau guau")

class Persona:
    def atrapar(self,pato):
        pato.caminar()
        pato.hablar()
        print("Lo atrape!")
        
pato = Pato()
perro = Perro()
persona = Persona()

# Al printear la informacion que nos arroja, nos permite saber que animal es
persona.atrapar(pato)
# El perro esta caminando
# El perro esta haciendo guau guau
# Lo atrape!