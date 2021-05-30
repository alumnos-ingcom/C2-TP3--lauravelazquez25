################
# Laura Velazquez- @lauravelazquez25
# 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Numeros positivos y negativos

def signo(numero):
    if numero < 0:
        return ('El numero es negativo')
    elif numero == 0:
        return ('El numero es cero')
    else:
        return ('El numero es positivo')
    

def prueba():
    ingreso = int(input('Ingrese un numero: '))
    print(signo (ingreso))    
    
    
if __name__ == "__main__":
    prueba()
    