################
# Laura Velazquez   @lauravelazquez25
# Ejercicio N°8
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Ordenar 3 valores


def ordenar_menor_a_mayor(uno,dos,tres):
    tupla= uno, dos, tres
    for k in range(1,len(tupla)):
        print(k)
        for i in range(0,len(tupla)-k):
            if tupla[i] > tupla [i+1]:
                auxiliar = tupla [i]
                tupla[i] = tupla[i+1]
                tupla[i+1] = auxiliar
    return tupla
    

def prueba():
    num1 = int(input('Ingrese un numero :'))
    num2= int(input('Ingrese un numero :'))
    num3 = int(input('Ingrese un numero :'))
    
    #tupla = num1,num2,num3
    print(ordenar_menor_a_mayor(num1,num2,num3))
    

if __name__ == "__main__":
    prueba()  
        