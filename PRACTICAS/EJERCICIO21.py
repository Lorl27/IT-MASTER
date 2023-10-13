#Escribir un programa que permita ingresar dos números enteros e 
# indicar si el primero es mayor, menor o igual al segundo.

def numeritos():
    num1=float(input("Ingresa el 1er num: "))
    num2=float(input("Ingresa el 2do num: "))
    
    if num1<num2:
        print(f"{num1} es menor a {num2}")
    elif num1>num2:
        print(f"{num1} es mayor a {num2}")
    else:
        print("Los 2 números son iguales")

numeritos()