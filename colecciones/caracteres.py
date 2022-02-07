path_words = "resources/words.txt"
exit = False

while exit == False:
    print("\nEscribe (0) para salir del programa.")
    print("Escribe (1) para introducir una nueva palabra.")
    print("Escribe (2) si quieres mostrar los nombres que tienen 5 o más caracteres.\n")
    
    menu_opt = int(input())
    if menu_opt == 0:
        exit = True
    if menu_opt == 1:
        words_file_add = open(path_words,"a")
        str = "\n"+input("Introduce la palabra a guardar: ")
        words_file_add.write(str)
        words_file_add.close()
        pass
    if menu_opt == 2:
        print("\nMostrando nombres con 5 o más caracteres:")
        words_file_read = open(path_words,"r")
        for line in words_file_read:
            if len(line.rstrip()) >= 5:
                print(line.rstrip())
        words_file_read.close()
