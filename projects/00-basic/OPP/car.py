# Pueden tener combinanciones de atributos o metodos
class Car:

    def __init__(self, marca, modelo, ano, color):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color

    # self se refiere al objecto que esta utilizando este objecto
    def encedido(self):
        print('El auto esta encedido!')

    def apagado(self):
        print('El auto esta apagado!')