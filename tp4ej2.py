################
# Laura Velazquez - @lauravelazquez25
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Suma lenta
def suma_lenta(numero, otro_numero):
    contador = 0
    if numero >= 0 and otro_numero >= 0:
        while contador< otro_numero:
            contador = contador +1
            suma = numero + contador
            print(suma)
            
    elif numero >0 and otro_numero < 0:
        while abs(contador)< abs(otro_numero):
            contador = contador -1
            suma = numero + contador
            print(suma)
            
    elif numero < 0 and otro_numero > 0 :
        while contador < otro_numero:
            contador = contador + 1
            suma = numero + contador
            print (suma)
            
    elif numero < 0 and otro_numero == 0:
        while abs(contador)< abs(numero):
            contador = contador +1
            suma = otro_numero - contador
            print(suma)        
            
    else:
        while abs(contador)< abs(otro_numero):
            contador = contador -1
            suma = numero + contador
            print(suma)
        
        
            

def prueba():
    """Este programa realiza la suma lenta entre dos numeros enteros,
        mostrando las sumas parciales"""
    
    num1 = int(input('Ingrese un numero : '))
    num2 = int(input('Ingrese otro numero: '))
    print('La suma lenta es :')
    print (suma_lenta(num1,num2))
       

if __name__ == "__main__":
    prueba()