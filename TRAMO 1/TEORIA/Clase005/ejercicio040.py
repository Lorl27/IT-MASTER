"""
Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b. 
(donde a <= b) 
El programa debe mostrar:
La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.
"""

a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))
while a > b: # ERROR
    print(f"Error: {a} tiene que ser <= {b}")
    b = int(input("Ingrese un valor para b: "))

producto_impares = 1
suma_pares = 0
for numero in range(a,b+1):
    print(numero,end=',')
    if numero % 2 == 0:
        suma_pares += numero
    else:
        producto_impares  *= numero

print()
print(f"Suma de pares : {suma_pares}")
print(f"Producto de impares : {producto_impares}")


