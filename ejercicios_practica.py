#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    if numero_1 > numero_2:
        print("El nro. ", numero_1, ", es mayor que el ", numero_2,".")
    else:
        print("El nro. ", numero_2, ", es mayor que el ", numero_1,".")

    # Imprima en pantalla según corresponda

    # Verifique si el numero_1 positivo, negativo o cero
    if numero_1 > 0:
        print("Todo nro. mayor a 0 es positivo.")
    elif numero_1 < 0:
        print("Todo nro. menor a 0 es negativo.")
    elif numero_1 == 0:
        print("Al ser igual a 0, se lo considera un numero neutro.")

    # Imprima el resultado en cada caso

    # Verifique si el numero_1 es mayor a 0 y menor a 100

    if numero_1 > 0 and numero_1 < 100:
        print( "El", numero_1, "es un numero mayor que 0 y menor que 100.")

    # Imprima en pantalla si se cumple o no la condición

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 < 10 and numero_2 > -2:
        print ("El", numero_1, "es menor que 10 y el", numero_2, "es mayor a - 2")
    elif numero_1 > 10:
        print( "El", numero_1, "es mayor que 10 y mayor que -2.")
    elif numero_2 < -2:
        print("El numero es menor que -2.")




def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    
    if texto_1 > texto_2:
        print("Alfabeticamente la palabra {} es mayor que la palabra {}.\n".format(texto_1,texto_2))
    elif texto_2 > texto_1:
        print("Alfabeticamente la palabra {} es mayor que la palabra {}.\n".format(texto_1,texto_2))
    else:
        if texto_1 == texto_2:
            print("La palabra {} y la palabra {} tienen el mismo valor alfabetico.\n".format(texto_1,texto_2))
   
   # Compare cual de las dos palabras tiene mayor # cantidad de letras
    if len (texto_1) > len (texto_2):
        print ("En termino de caracteres, la palabra {} es mayor que la palabra {}.\n".format(texto_1, texto_2))
    elif (texto_1) < (texto_2):
        print("En termino de caracteres, la palabra {} es mayor que la palabra {}.\n".format(texto_2,texto_1))
    else:
        print("La palabra {} es igual que la palabra {}.\n".format(texto_2,texto_1))
   
    # Imprima en pantalla según corresponda

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    if (texto_1[0]) > (texto_2[0]):
        print(
            "El primer caracter de la palabra {}, es mayor que el de la palabra {}.\n".format(texto_1,texto_2)
        )
    elif (texto_1[0]) < (texto_2[0]):
        print(
            "El primer caracter de la palabra {}, es menor que el de la palabra {}.\n".format(texto_1,texto_2)
        )
    elif (texto_1[0]) == (texto_2[0]):
        print(
            "El primer caracter de ambas palabras es igual.\n"
        )   

    copia_texto_1 = texto_1 

    if copia_texto_1 == texto_1 and texto_2 != copia_texto_1:
        print ("True")
    elif copia_texto_1 == texto_1 and texto_2:
        print("Tanto {} (texto_1) como {}(texto_2) y {}(copia_texto_1) son iguales".format(texto_1,texto_2,copia_texto_1))   
    else:
        print("{} es diferente a {}.\n".format(texto_1, texto_2)) 
    
    # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = int(input())
    numero_2 = int(input())

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"

    if numero_1 > numero_2:
        print("El numero {} es mayor que el numero {}.\n".format(numero_1,numero_2))
    elif numero_1 < numero_2:
        print("El numero {} es menor que el numero {}.\n".format(numero_1,numero_2))
    elif numero_1 == numero_2:
        print("Ambos numeros son iguales".format(numero_1,numero_2))
    if numero_2 < 0:
        print ("El numero {} es negativo.\n".format(numero_2))
    elif numero_2 > 0:
        print ("El numero {} es positivo.\n".format(numero_2))
    elif numero_2 == 0:
        print ("El numero {} es neutro.\n".format(numero_2))

    print("##################0#################\n")


    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 < 5 and numero_2 > 5:
        print("El numero {} no es mayo a 5 y el numero {} si es mayor a 5.\n".format(numero_1, numero_2))
    elif numero_1 < 5 and numero_2 < 5:
        print("Tanto numero {}, como numero {} son menores a 5.\n".format(numero_1, numero_2))
    elif numero_1 < 5 and numero_2 == 5:
        print("El numero {} es mayor a 5 y el nuemro {} es igual que 5.\n".format(numero_1, numero_2))    
    else:
        print("El numero {} es mayor a 5 y el nuemro {} es menor que 5.\n".format(numero_1, numero_2))
    
    
    
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    if puntaje >= 90:
        print ("A")
    # Si el puntaje es mayor igual a 80 --> imprimir B
    elif puntaje >= 80:
        print ("B")
    # Si el puntaje es mayor igual a 70 --> imprimir C
    elif puntaje >= 70:
        print("C")
    # Si el puntaje es mayor igual a 60 --> imprimir D
    elif puntaje >= 60:
        print("D")
    # Si el puntaje es manor a  60      --> imprimir F
    elif puntaje < 60:
        print("F")

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


def ej4():
# Ejemplos variables de texto
   # Verifique cual cual de los dos textos es mayor alfabéticamente
   
    # Imprima en pantalla según corresponda


    texto_1 = '5'
    texto_2 = '7'
    
    if texto_1 > texto_2:
        print("Alfabeticamente el texto {} es mayor que el texto {}.\n".format(texto_1, texto_2))
    else: 
        print("{} es alfabeticamente mayor que {}.\n".format(texto_2,texto_1))
    
    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    
    pase_int_t1 = int(texto_1)
    pase_int_t2 = int(texto_2)

    print("Se transformo la variable texto_1 a:", pase_int_t1, "y se transformo la variable texto_2 a:", pase_int_t2, ".\n")
    
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    if pase_int_t1 > pase_int_t2:
        print("Numericamente el {} es mayor que el {}.\n".format(pase_int_t1,pase_int_t2))
    elif pase_int_t1 == pase_int_t2:
        print("Ambos numeros son iguales.\n")
    else:
        print ("Numericamente el {} es menor que el {}.\n".format(pase_int_t1, pase_int_t2))
    
    # Imprima en pantalla según corresponda

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
    
    #Strings are compared lexicographically (by the character set code point values returned
    #by ord), and character by character until the end or first mismatch ("abc"
    #< "ac").


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python\n")
    ej1()
    ej2()
    ej3()
    ej4()
