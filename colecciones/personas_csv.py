import random
import csv

path_people = "resources/people.csv"
exit = False

while exit == False:
    print("\nPresiona (0) para salir del programa.")
    print("Presiona (1) para introducir una nueva persona.")
    print("Presiona (2) para mostrar una persona al azar.\n")
    
    menu_opt = int(input())
    if menu_opt == 0:
        exit = True
    if menu_opt == 1:
        words_file_add = open(path_people,"a", encoding="utf8")
        str = "\n"+input("Introduce el nombre de la persona: ")
        words_file_add.write(str)
        words_file_add.close()
        pass
    if menu_opt == 2:
        print("\nMostrando persona al azar:")
        words_file_read = open(path_people,"r", encoding="utf8")
        reader = csv.reader(words_file_read)
        row_list = list(reader)
        rand = int(random.randrange(0,len(row_list)))
        print(repr(row_list[rand][0]))
        words_file_read.close()