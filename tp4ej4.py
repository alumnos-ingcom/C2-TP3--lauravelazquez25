################
# Laura Velazquez- @lauravelazquez25
# 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Comparacion de numeros

def compara(numero, otro_numero):
    if numero < otro_numero:
        return numero
    elif numero == otro_numero:
        return ('son iguales')
    else:
        return otro_numero
                


def prueba():
    numero = int(input('Ingrese un numero: '))
    otro_numero = int (input('Ingrese otro numero: '))
    comparacion = compara(numero, otro_numero)
    print (f'El menor de los numeros es: {comparacion}')
                   

if __name__ == "__main__":
    prueba()