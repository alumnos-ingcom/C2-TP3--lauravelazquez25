###############
# Laura Velazquez   @lauravelazquez25
# Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Palindromo

def palindromo(texto):
    palabra_invertida = texto[::-1]
    if texto == palabra_invertida:
        return True
    else:
        return False


def prueba():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    prueba()