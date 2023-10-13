#Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/').
# Debe mostrarse el resultado para la operación ingresada.
# Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

def suma(a,b):
    return a+b

def multip(a,b):
    return a*b

def resta(a,b):
    return a-b

def div(a,b):
    return a/b

def operaciones():
    a= int(input("Ingrese el valor para el primer número:"))
    b= int(input("Ingrese el valor para el segundo número:"))

    valor_i=int(input("""INGRESÉ ALGUNO DE LOS SIGUIENTES VALORES:
                        1. SUMA
                        2. RESTA
                        3. MULTIPLICAR
                        4. DIVISIÓN
                        5.SALIR
                        """))

    while valor_i!=5:
        if valor_i == 1:
            print(suma(a,b))
            operaciones()
        elif valor_i == 2:
            print(resta(a,b))
            operaciones()
        elif valor_i == 3:
            print(multip(a,b))
            operaciones()
        elif valor_i == 4:
            if b==0:
                print("ERROR -- Dividir por 0 es imposible.")
                break
            else:
                print(div(a,b))
                operaciones()
        else:
            print("VALOR INTRODUCIDO ÉRRONEO.")
            break

operaciones()

