#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números\n')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    print ("Ingrese el valor numerico de la variable numero 1\n")
    num_1 = int(input())

    print ("Ingrese el valor numerico de la variable numero 2\n")
    num_2 = int(input())

    print ("Ejericio 1:\n")
   

    diferencia = num_1 - num_2

    if diferencia > 0:
        print ("El numero {} es positivo.\n".format(diferencia))
    elif diferencia == 0:
        print ("El numero {} es un valor neutro.\n".format(diferencia))
    else:
        print ("El valor {} es negativo.\n".format(diferencia))    

    print("_________________________________________________\n")


def ej2():
    print('Ejercicios de práctica con números\n')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    print ("Ingrese el valor numerico de la variable numero 1\n")
    num_1 = int(input())

    print ("Ingrese el valor numerico de la variable numero 2\n")
    num_2 = int(input())

    print ("Ingrese el valor numerico de la variable numero 2\n")
    num_3 = int(input())

    print ("Ejericio 2:\n")
   
    if num_1 % 2 == 0:
        print ("El  {} es un numero Par.\n".format(num_1))
    else:
        print("El {} es un numero Impar.\n".format(num_1) )
    if num_2 % 2 == 0:
        print ("El {} es un numero Par.\n".format(num_2))
    else:
        print("El {} es un numero Impar.\n".format(num_2) )
    if num_3 % 2 == 0:
        print ("El {} es un numero Par.\n".format(num_3))
    else:
        print("El {} es un numero Impar.\n".format(num_3) )    
   

    print("_________________________________________________\n")

def ej3():
    print('Ejercicios de práctica con números\n')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    print ("Ejericio 3:\n")
    print(" Bienvenido a la Calculadora de Inove.\n Siga los siguientes pasos para operar:\n")

    print (" Ingrese el primer valor con el que desea operar.\n")
    num_1 = int(input())

    print (" Ingrese el segundo valor \n")
    num_2 = int(input())

    print (" Ingrese el simbolo de la operacion deseada: +, -, *, /, o **(potencia)\n")
    operacion= str(input())

    suma = ('+')
    resta = ('-')
    multiplicación = ('*')
    división = ('/')
    potencia = ('**')

    if operacion == suma:
        print ("{} + {} =".format(num_1,num_2), int(num_1) + int(num_2))
    elif operacion == resta:
        print ("{} - {} =".format(num_1,num_2), int(num_1) - int(num_2))
    elif operacion == multiplicación:
        print ("{} * {} =".format(num_1,num_2), int(num_1) * int(num_2))
    elif operacion == división:
        print ("{} / {} =".format(num_1,num_2), int(num_1) / int(num_2))
    elif operacion == potencia:
        print ("{} ** {} =".format(num_1,num_2), int(num_1) ** int(num_2))
    else:
        print("No ha seleccionado ninguna de las opciones permitidas\n")
        
        
        print("_________________________________________________\n")       


def ej4():
    print('Ejercicios de práctica con cadenas\n')

    print ("Ejericio 4:\n")

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    print("Ud. ingresara 3 plabras a eleccion a traves del siguiente programa:\n")
    
    palabra_1 = str(input())
    palabra_2 = str(input())
    palabra_3 = str(input())

    print("Usted eligio las siguientes palabras:\n")
    palabras_ele = (palabra_1, palabra_2, palabra_3)    
    print (palabras_ele, "\n")

    orden_alfa = ("1")
    orden_q = ("2")

    print(" Si Ud. desea ordenar las palabras Alfabeticamente ingrese 1 \n o ingres 2 si desea ordenarlas por cantidad de letras.\n")
    eleccion= str(input())

    if eleccion == orden_alfa:
        print ("Orden alfabetico:",sorted(palabras_ele))
    elif eleccion == orden_q:
        print ("Orden cantidad de letras:", sorted(palabras_ele, key=len, reverse=True))
    else:
        print ("La opcion ingresada no es valida\n")

    '''
    Comentarios: Claramente no use los signos > y < para hacer el ejercicio
    porque me costo salir de la idea de como lo habia pensado, cada vez me empantanaba 
    mas y decidi darle una solucion creando una tupla y luego obteniendo el resultado
    en forma de lista.
    De todas formas, use condicionales.     
    '''

    print("_________________________________________________\n")


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
