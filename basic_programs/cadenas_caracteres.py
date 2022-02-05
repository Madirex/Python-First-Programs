phrase = input("Introduce una oración: ")
print("Longitud de la cadena:\n",len(phrase),"\n")
print("Espacios en blanco:\n", phrase.count(" ",0,len(phrase)),"\n")
print("Oración en mayúsculas:\n", phrase.upper(),"\n")
print("Cadena duplicada:\n",(phrase+"\n")*2)
print("Cadena dividida en una lista de palabras:","\n")
num = 0
for p in phrase.split(" "):
    num +=1
    print(num,p)