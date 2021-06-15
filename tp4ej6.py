################
# Laura Velazquez - @lauravelazquez25
# Ejercicio 6 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


### Maximo/Minimo


import listasaleatorias

def minimo(lista):
    aleatoria = ()
    temporaria = 0
    for i in range(1,len(aleatoria)):
        for posicion in range(len(aleatoria)-i):
            if aleatoria(posicion) < aleatoria(posicion+1):
                temporaria = aleatoria[posicion]
                aleatoria[posicion] = aleatoria[posicion+1]
                aleatoria[posicion] = temporaria
                
    return temporaria
        
 
def prueba():
    aleatoria = lista_random()
    print('Esta funcion retorna el menor de los elementos de una lista aleatoria')
    el_minimo = minimo(aleatoria)
    print(f'La lista aleatoria es {aleatoria}')
    print(f'La lista aleatoria es {el_minimo}')
    
    

if __name__ == "__main__":
    prueba()      