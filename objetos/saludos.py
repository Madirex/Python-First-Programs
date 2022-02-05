import random

class Saludo:
    def formal(name = ""):
        print("Hola",name)
    def informal(name = ""):
        print("Hi",name)
    def aleatorio(name = ""):
        lista_saludos = ["Buenas tardes","Un placer,","Buenos días","hola","hi"]
        print(lista_saludos[int(random.randrange(0,len(lista_saludos)))],name)

if __name__ == "__main__":
    name = input("Introduce tu nombre:")
    Saludo.formal(name)
    Saludo.informal(name)
    Saludo.aleatorio(name)