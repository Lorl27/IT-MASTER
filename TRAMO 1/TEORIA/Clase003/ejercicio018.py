"""
Ejercicio 018
Escribir un programa que permita al usuario ingresar un número entero y luego muestre un mensaje indicando si el número es par o impar.

Pensando los pasos para resolver el problema:

-1 Pedir al usuario que ingrese un número entero.

-2 Almacenar ese número en una variable.

-3 Verificar si el número es par o impar.

Si el número es par, mostrar un mensaje indicando que es par.
Si el número es impar, mostrar un mensaje indicando que es impar.
(Para verificar si un número es par o impar, se puede utilizar el operador módulo (%). Si el resto de la división del número por 2 es 0, entonces el número es par. Si el resto de la división del número por 2 es 1, entonces el número es impar.)
"""

numero = int(input("Numero: "))

es_par =  numero%2 == 0

print(f"numero: {numero} ¿Es par? ==> {es_par} ")

#   True  == True 
if es_par == True:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} no es par")

if es_par:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} no es par")
