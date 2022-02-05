from datetime import date
actual_year = date.today().year
continue_str = "(Presiona enter para continuar con las instrucciones)"

print("Haz las siguientes operaciones 🧙...")
print("(no me digas las operaciones) 🤫 deberás de calcularlas tú y al final de todo decirme el número que has obtenido.")
input("A tu talla de pie multiplícale el número de dedos de una mano "+continue_str)
input("Ahora a ese número súmale 50 "+continue_str)
input("Multiplica el número que has calculado por 20 "+continue_str)
print("A continuación, súmale" , actual_year - 1000 ,"y réstale tu año de nacimiento.")
answer = input("Escribe el número que has obtenido: ")
print("Calculo que tu talla de zapato 👠 es",answer[:-2],"y tu edad es",answer[2:], "🧙")