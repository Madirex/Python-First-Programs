#Calcular el factorial de un número pasado por consola
def factorial(n):
    n = int(n)
    fact = 1
    while n > 1:
        fact *=n
        n -=1
    return fact

if __name__ == '__main__':
    print("El factorial del número introducido es",factorial(input("Introduce un número para calcular su factorial:")))