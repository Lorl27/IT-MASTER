#Escribir un programa que solicite al usuario ingresar tres numeros enteros.
# El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera:
# "[numero1] + [numero2] + [numero3] = [suma]".

num1= int(input("Ingrese número 1: "))
num2= int(input("Ingrese número 2: "))
num3= int(input("Ingrese número 3: "))

suma= num1+num2+num3

print(f"{num1} + {num2} + {num3} = {suma} ")