#Escribir un programa que permita ingresar un número entero.
# Debe mostrarse el número ingresado:

#a. Multiplicado por 10. (utilizar el operador *)
# a. Dividido por 10. (utilizar el operador /)
# a. Elevado al cuadrado. (utilizar el operador **)

#Cada resultado debe mostrarse en una línea distinta.

a = int(input("Ingrese un número a continuación: "))
print( a*10 , a/10 , a**2 , sep="\n" )