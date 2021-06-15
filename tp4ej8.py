################
# Laura Velazquez   @lauravelazquez25
# Ejercicio N°8
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Ordenar 3 valores


def ordenar_menor_a_mayor(uno,dos,tres):
    ingreso = [uno,dos,tres]
    if uno < dos and dos < tres:
        ingreso = [uno, dos ,tres]
        return tuple(ingreso)

    elif uno < tres and tres < dos:
        ingreso = [uno, tres,dos]
        return tuple(ingreso)
    
    elif dos < uno and uno < tres:
        ingreso = [dos,uno, tres]
        return tuple(ingreso)
    
    elif dos < tres and tres < uno:
        ingreso = [dos,tres,uno]
        return tuple(ingreso)
    else:
        ingreso = [tres,dos,uno]
        return tuple(ingreso)
    return ()
       
    


def prueba():
    num1 = int(input('Ingrese un numero :'))
    num2= int(input('Ingrese un numero :'))
    num3 = int(input('Ingrese un numero :'))
    ordenado = ordenar_menor_a_mayor(num1 ,num2 ,num3)
    print (ordenado)
    
    

if __name__ == "__main__":
    prueba()   
##        
