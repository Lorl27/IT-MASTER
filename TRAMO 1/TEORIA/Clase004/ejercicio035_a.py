"""
Ejercicio 035
Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.

b) El número es impar.

A partir de estas reglas, escribir un programa que permita ingresar un número entero.

Debe asignar el valor que corresponda a las variables booleanas:
esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno

el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.
"""
numero = int(input("Numero: "))

# a) El número es de un solo dígito.
esDeUnSoloDigito = numero >= -9 and numero <= 9

# b) El número es impar.
esImpar = (numero%2) != 0

estaEnAmbos = esDeUnSoloDigito and esImpar

noEstaEnNinguno = not esDeUnSoloDigito and not esImpar

cartel = f"""
Numero: {numero}
esDeUnSoloDigito {esDeUnSoloDigito}
esImpar {esImpar}
estaEnAmbos {estaEnAmbos}
noEstaEnNinguno {noEstaEnNinguno}

"""
print(cartel)

print(f"1 <= 5 <= 10 {1 <= 5 <= 10}")