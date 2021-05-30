################
# Laura Velazquez   @lauravelazquez25
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Restas Sucesivas


def division_lenta (dividendo, divisor):    
    if (dividendo > 0 & divisor >0 ):
            cociente = 0
            residuo = dividendo - divisor
            while residuo >=0 :
                residuo = residuo - divisor
                cociente = cociente +1
            return (cociente)
        
    elif (dividendo > 0 & divisor < 0 ):
            cociente = 0
            residuo = dividendo - divisor
            while abs(residuo) >=0 :
                residuo = residuo - abs(divisor)
                cociente = cociente +1
            return (cociente *(-1))
        
    elif (dividendo < 0 & divisor < 0 ):
            cociente = 0
            residuo = dividendo - divisor
            while abs(residuo) >=0 :
                residuo = abs(residuo) - abs(divisor)
                cociente = cociente +1
            return (cociente )
    else:
        cociente = 0
        residuo = dividendo - divisor
        while abs(residuo) >=0 :
            residuo = abs(residuo) - abs(divisor)
            cociente = cociente +1
        return (cociente )
        
 
def prueba():
    print ('Este programa realiza la division entre dos numeros enteros')
    dividendo = int(input('Ingrese el Dividendo : '))
    divisor = int(input('Ingrese el divisor : '))
    
    print ('El cociente es : ', division_lenta(dividendo , divisor))
    resto= dividendo - (division_lenta(dividendo, divisor) * divisor)
    print ('el resto es: ', resto)
    

if __name__ == "__main__":
    prueba()    
    