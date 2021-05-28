################
# Laura Velazquez - @lauravelazquez25
#
# UNRN Andina - Introducción a la Ingenieria en Computación
################


### Conversion de temperaturas
def convertir_a_farenheit(centigrados):
    temp_farenheit = (centigrados * 5/9 ) + 32
    return temp_farenheit


def convertir_a_centigrados(farenheit):
    temp_centig = (farenheit -32 ) * 5/9
    return temp_centig


def prueba():
    menu =""" Este programa le permite convertir temperaturas en grados centigrados a farenheit y viceversa'
Elija una opcion:
1-Farenheit a Centigrados
2-Centigrados a Farenheit"""
    if menu =='1':
        temperatura1= int(input('Ingrese la temperatura en grados farenheit: '))
        print ('La temperatura corresponde a ',convertir_a_centigrados(temperatura1), 'grados centigrados')
    elif menu =='2':
        temperatura2 = int(input('Ingrese la temperatura en grados centigrados: '))
        print ('La temperatura corresponde a ', convertir_a_farenheit(temperatura2), 'grados farenheit')

if __name__ == "__main__":
    prueba()