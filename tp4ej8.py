################
# Laura Velazquez   @lauravelazquez25
# Ejercicio N°8
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Ordenar 3 valores


def ordenar_mayor_a_menor(uno,dos,tres):
    tupla= uno, dos, tres
    if tupla[0] < tupla[1] and tupla[1] < tupla[2]:
        tupla_menor_a_mayor = tupla[0],tupla[1],tupla[2]
        return tupla_menor_a_mayor
    
    #elif  < tres and 
        
    


def prueba():
    num1 = int(input('Ingrese un numero :'))
    num2= int(input('Ingrese un numero :'))
    num3 = int(input('Ingrese un numero :'))
    
    tupla = num1,num2,num3
    print(ordenar_mayor_a_menor(num1,num2,num3))
    

if __name__ == "__main__":
    prueba()   
        
