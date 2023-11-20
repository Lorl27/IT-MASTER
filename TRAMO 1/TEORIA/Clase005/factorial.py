


"""
n! ==> n*(n-1)!
         (n-1)*(n-2)!
               (n-2)*(n-3)!
1! = 1
0! = 1                
"""
"""import sys
sys.set_int_max_str_digits(100000)
numero = int(input("Numero: "))
copia = numero
producto = 1
while numero > 0:
    producto *= numero
    numero -= 1
print(f"El factorial de {copia} es {producto} y tiene {len(str(producto))}")

"""
numero = int(input("Ingrese un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"EL FACTORIAL DE {numero} ES {factorial} Y TIENE {len(str(factorial))}") 

