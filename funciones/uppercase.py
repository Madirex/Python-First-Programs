def first_and_last_upper_word(word):
    return word.title()[:-1] + word[-1].upper()

if __name__ == '__main__':
    print("Programa que dada una palabra, convierte todas las letras en minúsculas a excepción de la primera y la última letra, las cuales serán convertidas en mayúscula.")
    print(first_and_last_upper_word(input("Introduce una palabra:")))