"""
Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de un 
alumno e indicar si promocionó, aprobó o debe recuperar. 

Si el valor de la nota no esta entre 0 y 10, debe informar un error.

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.

P	Q	(P or Q)
V	V	    V
V	F	    V
F	V	    V
F	F	    F

"""

nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
#               7            7              2           2
error_datos = nota1 < 0 or nota1 > 10 or  nota2 < 0 or nota2 > 10

if not error_datos:
    aprueba = nota1 >= 4 and nota2 >= 4
    recupera = not aprueba
    promociona = nota1 >= 7 and nota2 >= 7

    if not aprueba:
        cartel = "Recupera"
    else: 
        cartel = "Aprueba" 
        if promociona:
            cartel += " con promoción"
else:
    cartel = "Error de datos"

print(cartel)