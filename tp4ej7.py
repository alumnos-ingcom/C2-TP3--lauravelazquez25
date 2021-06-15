################
# Laura Velazquez   @lauravelazquez25
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Restas Sucesivas


def division_lenta (dividendo, divisor):
    cociente = 0
    residuo = dividendo - divisor
    
    while residuo >=0 :
        residuo = residuo - divisor
        cociente = cociente +1
    return (cociente)


def prueba():
    print ('Este programa realiza la division entre dos numeros enteros')
    dividendo = int(input('Ingrese el Dividendo : '))
    divisor = int(input('Ingrese el divisor : '))
    
    if dividendo >0 & divisor >0:
        print ('El cociente es : ', division_lenta(dividendo , divisor))
        resto= dividendo - division_lenta(dividendo, divisor) * divisor
        print ('el resto es: ', resto)
    elif (dividendo < 0 & divisor >0) :
        dividendo = dividendo *(-1)
        print ('El cociente es : ', division_lenta(dividendo , divisor)*(-1))
        resto= (dividendo - division_lenta(dividendo, divisor) * divisor) * (-1)
        print ('el resto es: ', resto)
        
    elif (dividendo > 0 & divisor < 0):
        print ('El cociente es : ', division_lenta(dividendo , divisor)*(-1))
        resto= dividendo - division_lenta(dividendo, divisor) * divisor
        print ('el resto es: ', resto)
        
    else:
        print ('El cociente es : ', division_lenta(dividendo , divisor))
        resto= ((dividendo - division_lenta(dividendo, divisor) * divisor))*(-1)
        print ('el resto es: ', resto)    

if __name__ == "__main__":
    prueba()