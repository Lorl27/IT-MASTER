#Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y
# el valor que esta en medio.

#Ejemplo: Si se ingresan los números 5, 3 y 7,
# el programa debe mostrar el número 5 como el menor, el número 7 
# como el mayor y el número 3 como el que esta en medio

def numeritos():
    num1=float(input("Ingresa el 1er num: "))
    num2=float(input("Ingresa el 2do num: "))
    num3=float(input("Ingresa el 3er num: "))
    
    
    if num1<num2 and num1<num3:
        print(f"{num1} es menor a {num2} y {num3}")
    elif num1>num2 and num1>num3:
        print(f"{num1} es mayor a {num2} y {num3}")
    elif num1>num2 and num1<num3:
        print(f"{num1} es mayor a {num2} pero menor a {num3}. ergo {num2} esta en el medio")
    elif num1>num3 and num1<num2:
        print(f"{num1} es mayor a {num3} pero menor a {num2}. ergo {num3} esta en el medio ") #bucle
    elif num2<num1 and num2<num3:
        print(f"{num2} es menor a {num1} y {num3}")
    elif num2>num3 and num2> num1:
        print(f"{num2} es mayor a {num1} y {num3}")
    elif num2>num1 and num2<num3:
        print(f"{num2} es mayor a {num1} pero menor a {num3}. ergo {num1} esta en el medio")
    elif num2>num3 and num2<num1:
        print(f"{num2} es mayor a {num3} pero menor a {num1}. ergo {num3} esta en el medio") #bucle
    elif num3<num1 and num3<num2:
        print(f"{num3} es menor a {num1} y {num2}")
    elif num3>num2 and num3> num1:
        print(f"{num3} es mayor a {num1} y {num2}")
    elif num3>num1 and num3<num2:
        print(f"{num3} es mayor a {num1} pero menor a {num2} ergo {num2} esta en el medio")
    elif num3>num2 and num3<num1:
        print(f"{num3} es mayor a {num2} pero menor a {num1}. ergo {num1} esta en el medio") #bucle
    else:
        print("Los 3 números son iguales")

numeritos()