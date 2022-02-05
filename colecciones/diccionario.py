import csv

path_people = "resources/dictionary.csv"

def remove_row(n):
    if n != -1:
        new_csv = list()
        removed = ""
        with open(path_people, 'r', encoding="utf8") as readFile:
            reader = csv.reader(readFile)

            row_num = 0
            for row in reader:
                if row_num != n:
                    new_csv.append(row)
                else:
                    removed = row
                row_num +=1

        with open(path_people, 'w', encoding="utf8") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(new_csv)
        print("\nLa siguiente definición ha sido eliminada ❌ correctamente:")
        print(row,"\n")

def print_row_csv(n):
    if n != -1:
        words_file_read = open(path_people,'r', encoding="utf8")
        csv_reader = csv.reader(words_file_read, delimiter=';')
        row_list = list(csv_reader)
        print(repr(row_list[n][0]))
        print(repr(row_list[n][1]))

def search(search_word):
    col = -1

    words_file_read = open(path_people,'r', encoding="utf8")
    csv_reader = csv.reader(words_file_read, delimiter=';')
    row_list = list(csv_reader)
    
    num = 0
    for n in row_list:
        if num > 0: # Evitar primera fila
            if repr(n[0]).lower() == "'" + search_word.lower() + "'":
                col = num
                
        num += 1

    words_file_read.close()

    if col == -1:
        print("No se ha encontrado la definición.")

    return col


if __name__ == '__main__':
    exit = False
    while exit == False:
        print("\nPresiona (0) para salir del programa.")
        print("Presiona (1) para consultar una definición.")
        print("Presiona (2) para introducir una nueva definición.")
        print("Presiona (3) para borrar una definición.\n")
    
        menu_opt = int(input())

        if menu_opt == 0:
            exit = True
        if menu_opt == 1:
            search_word = input("\nIntroduce el nombre de la palabra a consultar:")
            print_row_csv(search(search_word))
        if menu_opt == 2:
            words_file_add = open(path_people,'a',encoding="utf8", newline='')
            csv_writer = csv.writer(words_file_add, delimiter=';')
            str_word = str(input("Introduce el nombre de la palabra: "))
            str_def = str(input("Introduce el nombre de la definición: "))
            csv_writer.writerow([str_word,str_def])
            words_file_add.close()
            pass
        if menu_opt == 3:
            search_word = input("\nIntroduce el nombre de la palabra a borrar:")
            remove_row(search(search_word))