"""
Ejercicio 011
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado 
y qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, 
a partir de esto calcular e informar lo requerido previamente.

"""

nombre1 = input("Nombre: ")
capital1 = float(input("Capital $: "))

nombre2 = input("Nombre: ")
capital2 = float(input("Capital $: "))

nombre3 = input("Nombre: ")
capital3 = float(input("Capital $: "))

capital_total = capital1+capital2+capital3

por1 = capital1 *100 / capital_total
por2 = capital2 *100 / capital_total
por3 = capital3 *100 / capital_total

print("-"*150)
print("Compra del auto")
print("-"*150)
print(f"Total: {capital_total:20.2f}")
print("-"*150)

print(f"{nombre1:20} Capital: {capital1:10.2f} ==> {por1:6.2f}%")
print(f"{nombre2:20} Capital: {capital2:10.2f} ==> {por2:6.2f}%")
print(f"{nombre3:20} Capital: {capital3:10.2f} ==> {por3:6.2f}%")


