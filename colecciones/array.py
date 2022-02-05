# Crear una lista con contenido [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [54,72]]. Imprimir la lista, asignar valor cero a todos los elementos mayores a 50 y volver a imprimir la lista.
list = [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [54,72]]
print("\nImprimiendo lista:")
for l1 in list:
    for l2 in l1:
        print(l2)

print("\nImprimiendo lista con elementos mayores a 50 asignados a 0:")
for l1 in list:
    for l2 in l1:
        if l2 > 50:
            l2 = 0
        print(l2)