################
# Laura Velazquez- @lauravelazquez25
# 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Comparacion de numeros

def compara(numero, otro_numero):
    if numero < otro_numero:
        return ('-1')
    elif numero == otro_numero:
        return ('0')
    else:
        return ('1')
                


def prueba():
    numero = int(input('Ingrese un numero: '))
    otro_numero = int (input('Ingrese otro numero: '))
    
    print (compara(numero, otro_numero))
                   

if __name__ == "__main__":
    prueba()