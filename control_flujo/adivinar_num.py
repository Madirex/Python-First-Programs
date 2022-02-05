import random
min = 0
max = 100
exit = False
rand = random.randrange(0,100)

print("Intenta adivinar el número en el que estoy pensando...")
print("Será entre",min,"y",max)

while not exit:
    user_val = int(input("Introduce el número: "))
    if user_val == rand:
        print("\n¡Número correcto 👏!\n")
        exit = True
    if user_val < rand:
        print("\nNo has adivinado el número.\nEl número es más grande ⬆ que el que has introducido.\n")
    if user_val > rand:
        print("\nNo has adivinado el número.\nEl número es más pequeño ⬇ que el que has introducido.\n")