###############
# Laura Velazquez   @lauravelazquez25
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Restas Sucesivas


def division_lenta (dividendo, divisor):
    if divisor >0 and dividendo >0 :
        cociente = 1
        residuo = dividendo - divisor
        while residuo >= divisor :
            residuo = residuo - divisor
            cociente = cociente +1
        return (cociente,abs(residuo))
    
        
    elif (dividendo < 0 and divisor >0):
        cociente = 1
        residuo = dividendo + divisor
        while abs(residuo) >= divisor :
            residuo = residuo + divisor
            cociente = (cociente +1)
        return (-1*cociente, residuo)
    
    elif (dividendo < 0 and divisor < 0):
        cociente = 1
        residuo = dividendo - divisor
        while abs(residuo) >= abs(divisor) :
            residuo = residuo + abs(divisor)
            cociente = (cociente +1)
        return (cociente, residuo)
    
    else:
        cociente = 1
        residuo = dividendo - abs(divisor)
        while residuo >= abs(divisor) :
            residuo = residuo - abs(divisor)
            cociente = (cociente +1) 
        return (-cociente, residuo)       
  
def prueba():
    print ('Este programa realiza la division entre dos numeros enteros')
    dividendo = int(input('Ingrese el Dividendo : '))
    divisor = int(input('Ingrese el divisor : '))
    var1, var2 = division_lenta (dividendo, divisor)
    print ('El cociente es : ', var1)
    print ('el resto es: ', var2)
    
if __name__ == "__main__":
    prueba()
    