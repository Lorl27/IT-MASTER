# Para acceder a cierta atracción, alcanza con que se cumpla solamente una de las siguientes condiciones:
# ser mayor de 6 años o medir más de 1,50 metros.

# Escribir un programa en Python que solicite al usuario su edad y estatura, 
# y que determine si cumple con los requisitos para subir a la atracción.
# Si cumple con al menos una de las condiciones,
# el programa debe imprimir "¡Puede acceder!" en la pantalla. 
# Si no cumple con ninguna de las condiciones, el programa debe imprimir un mensaje que lo indique.

def juego():
    edad=int(input("Ingrese su edad: "))
    altura=float(input("Ingrese su altura: "))
    if edad>6 or altura>1.50:
        print("Usted puede subir")
    elif edad<=6:
        print("Demasiado jovr.NO")
    else:
        print("Demiasiado bajo. NO")

juego()