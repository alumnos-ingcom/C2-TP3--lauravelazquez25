################
# Laura Velazquez   @lauravelazquez25
# Ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Factores Primos

def factores_primos(numero):
    factores = []
    
    for i in range (2, numero+1):
        while numero % i ==0 :
            factores.append(i)
            numero = numero / i
    return tuple(factores)


def prueba():
    print ('Este programa realiza la descomposicion de un numero en sus factores primos')
    ingreso = int(input('Ingrese el numero a descomponer : '))
     
    print ('Los factores primos son: ', factores_primos(ingreso))

if __name__ == "__main__":
    prueba()    
                