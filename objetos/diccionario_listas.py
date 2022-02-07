# Reescribe el ejercicio 3 del apartado “Colecciones” con orientación a objetos. Opcional:
# Usa herencia para tener un diccionarios de al menos dos idiomas.
# Añade las opciones de importar o exportar el diccionario a un fichero.
import csv
path_people = "resources/dictionary2.csv"

class Dictionary:
    definitions = []

    def add_definition(self,word, definition):
        self.definitions.append(Definition(word, definition))
        print("Definición agregada.")
    
    def get_definition(self,word):
        for definition in self.definitions:
            if definition.get_word() == word:
                return definition.get_definition()

    def remove_definition(self,word):
        for definition in self.definitions:
            if definition.get_word() == word:
                self.definitions.remove(definition)
                print("Definición eliminada.")


    def export_csv(self):
        words_file_add = open(path_people,'a',encoding="utf8", newline='')
        csv_writer = csv.writer(words_file_add, delimiter=';')

        for l in self.definitions:
            str_word = str(l.get_word())
            str_def = str(l.get_definition())
            csv_writer.writerow([str_word,str_def])

        words_file_add.close()
        print("Datos exportados.")

class Definition:
    word = ""
    definition = ""

    def __init__(self, word, definition): 
        self.word = word
        self.definition = definition

    def show_definition(self):
        print("La definición de la palabra",self.word,"es:",self.definition)

    def get_word(self):
        return self.word

    def get_definition(self):
        return self.definition
    


if __name__ == "__main__":
    exit = False
    dictionary = Dictionary()
    while exit == False:
        print("\nEscribe (0) para salir del programa.")
        print("Escribe (1) para consultar una definición.")
        print("Escribe (2) para introducir una nueva definición.")
        print("Escribe (3) para borrar una definición.")
        print("Escribe (4) para exportar las definiciones.\n")
    
        menu_opt = int(input())

        if menu_opt == 0:
            exit = True
        if menu_opt == 1:
            search_word = input("\nIntroduce el nombre de la palabra a consultar:")
            print(dictionary.get_definition(search_word))
        if menu_opt == 2:
            str_word = str(input("Introduce el nombre de la palabra: "))
            str_def = str(input("Introduce el nombre de la definición: "))
            dictionary.add_definition(str_word, str_def)
            pass
        if menu_opt == 3:
            search_word = input("\nIntroduce el nombre de la palabra a borrar:")
            dictionary.remove_definition(search_word)
        if menu_opt == 4:
            dictionary.export_csv()
