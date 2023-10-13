"""
Ejercicio 036
Escribir un programa que permita ingresar dos números enteros y la operación 
a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación 
ingresada. 
Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').
"""



n1 = int(input("Operando 1: "))
n2 = int(input("Operando 2: "))
op = input("Operacion: ")
texto = f"{n1} {op} {n2} = "
if op in "+-*/":
    if op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 - n2
    elif op == '*':
        resultado = n1 * n2
    else:
        if n2 == 0:
            resultado = "Error"
        else:
            resultado = n1/n2
    texto += str(resultado)
else:
    texto += "Error" 

print(texto)

