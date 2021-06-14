################
# Laura Velazquez - @lauravelazquez25
# Ejercicio Conversor de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################


### Conversion de temperaturas
def convertir_a_farenheit(centigrados):
    temp_farenheit = (centigrados * 9/5 ) + 32
    temp_farenheit = round (temp_farenheit, 2)
    return temp_farenheit


def convertir_a_centigrados(farenheit):
    temp_centig = (farenheit -32 ) * 5/9
    temp_centig = round (temp_centig , 2)
    return temp_centig


def prueba():
    menu =int(input(""" Este programa le permite convertir temperaturas en grados centigrados a farenheit y viceversa'
    Elija una opcion:
    1-Farenheit a Centigrados
    2-Centigrados a Farenheit  """))
    
    if menu == 1:
        
        temperatura1= int(input('Ingrese la temperatura en grados farenheit: '))
        temperatura_convertida = convertir_a_centigrados(temperatura1)
        print ('La temperatura corresponde a ',temperatura_convertida, 'grados centigrados')
    elif menu == 2:
        temperatura2 = int(input('Ingrese la temperatura en grados centigrados: '))
        conversion_temperatura = convertir_a_farenheit(temperatura2)
        print ('La temperatura corresponde a ',conversion_temperatura , 'grados farenheit')

if __name__ == "__main__":
    prueba()
