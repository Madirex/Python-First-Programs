# Función que ordena los nombres por su longitud
def orderByLength(str):
    return sorted(str, key=len)
    
# Main
if __name__ == "__main__":
    list = []
    people_num = 5
    print("Introduce el nombre de",people_num,"personas:")
    string = "Introduce el nombre de la persona nº"
    for n in range(0,people_num,1):
        list.append(input(string + str(n+1) + ": "))

    print("\nLista de personas que has introducido (ordenada alfabéticamente):")
    list_sort = sorted(list)
    for e in list_sort:
        print(e)

    print("\nAhora se ordenarán según la longitud:")
    for e in orderByLength(list):
        print(e)