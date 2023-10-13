# Escribir un programa que permita al usuario ingresar dos números enteros.
# La computadora debe indicar si el mayor es divisible por el menor.

# (Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)

def div(a,b):
    if b<a and a%b==0:
        print(f"{a} es divisible con {b}")
    elif a<b and b%a==0:
        print(f"{b} es divisible con {a}")
    else:
        print("NO son divisibles [mayor x el menor]")
        
div(5,4); div(5,10); div(2,4)