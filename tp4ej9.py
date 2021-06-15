################
# Laura Velazquez   @lauravelazquez25
# Ejercicio 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Numeros Primos

def es_primo(numero):
    if numero ==1:
        return True
    elif numero < 0:
        abs_numero = abs(numero)
        for i in range (2 , abs_numero):
            if abs(numero) % i ==0:
                return False
        return True
    
    elif numero ==2:
        return True
        
    else:
        for i in range(2 ,numero ):
            if numero % i == 0:
                return False
        return True


def prueba():
    print ('Este programa indica si un numero ingresado es primo')
    numero = int(input('Ingrese un numero : '))
    salida= es_primo(numero)
    
    if salida == True:
        print ('El nro ingrsado es primo')
    else:
        print ('El nro ingresado no es primo ')        
    
    
if __name__ == "__main__":
    prueba()    
            
        
        
        