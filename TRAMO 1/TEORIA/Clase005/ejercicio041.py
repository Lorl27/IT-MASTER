"""
Ejercicio 041
Escribir un programa que lea números enteros hasta que se ingrese un 0, 
y muestre el máximo.
"""
from random import randint

maximo = -float('inf')
numero = randint(-10000,10000)
contador = 0
while numero != 0:
    contador += 1
    if numero > maximo:
        maximo = numero
    numero = randint(-10000,10000)
print(f"Maximo : {maximo} de {contador} numeros generados")

