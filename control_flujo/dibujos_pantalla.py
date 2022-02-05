print("Voy a dibujar un triángulo rectángulo isósceles...")
triangle_size = int(input("Introduce la altura que quieres que tenga: "))

for column in range(0,int(triangle_size)):
    print("\t"," "*(int(triangle_size) - column), "**"*column)

print("Ahora dibujaré un triángulo rectángulo escaleno...")
triangle_size = int(input("Introduce la altura que quieres que tenga: "))
for column in range(0,int(triangle_size)):
    print("\t","**"*column)