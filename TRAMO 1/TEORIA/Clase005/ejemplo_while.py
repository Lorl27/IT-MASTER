"""
Leer un grupo de datos enteros terminado con un cero.
Mostrar la suma.

g1 = 1,5,4,7,8,9,6,5,4,1,2,54,0
g2 = 1,2,54,0
g1 = 0

"""

# ANTES (PARA TODOS LOS DATOS)
suma = 0
numero = int(input("Numero: "))
while numero != 0:
    # DURANTE (PARA CADA DATO)
    suma += numero # suma = suma + numero (No nos gusta)
    numero = int(input("Numero: "))

# DESPUES (TOTALES)
print(f"Suma: {suma}")

