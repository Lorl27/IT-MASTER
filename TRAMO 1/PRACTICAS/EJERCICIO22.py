#Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.

def numeritos():
    num1=float(input("Ingresa el 1er num: "))
    num2=float(input("Ingresa el 2do num: "))
    num3=float(input("Ingresa el 3er num: "))
    
    
    if num1<num2 and num1<num3:
        print(f"{num1} es menor a {num2} y {num3}")
    elif num1>num2 and num1>num3:
        print(f"{num1} es mayor a {num2} y {num3}")
    elif num1>num2 and num1<num3:
        print(f"{num1} es mayor a {num2} pero menor a {num3}")
    elif num1>num3 and num1<num2:
        print(f"{num1} es mayor a {num3} pero menor a {num2}") #bucle
    elif num2<num1 and num2<num3:
        print(f"{num2} es menor a {num1} y {num3}")
    elif num2>num3 and num2> num1:
        print(f"{num2} es mayor a {num1} y {num3}")
    elif num2>num1 and num2<num3:
        print(f"{num2} es mayor a {num1} pero menor a {num3}")
    elif num2>num3 and num2<num1:
        print(f"{num2} es mayor a {num3} pero menor a {num1}") #bucle
    elif num3<num1 and num3<num2:
        print(f"{num3} es menor a {num1} y {num2}")
    elif num3>num2 and num3> num1:
        print(f"{num3} es mayor a {num1} y {num2}")
    elif num3>num1 and num3<num2:
        print(f"{num3} es mayor a {num1} pero menor a {num2}")
    elif num3>num2 and num3<num1:
        print(f"{num3} es mayor a {num2} pero menor a {num1}") #bucle
    else:
        print("Los 3 números son iguales")

numeritos()