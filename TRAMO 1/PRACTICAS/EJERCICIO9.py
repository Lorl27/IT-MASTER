#Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2.
# Una vez cargadas, mostrar ambas variables por pantalla,
# intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y
# volvé a mostrarlas actualizadas.

i=input()
m=input()
print(i,m)
i,m=m,i
print(i,m)