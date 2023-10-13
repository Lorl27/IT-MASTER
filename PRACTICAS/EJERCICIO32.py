# Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km
# que desea recorrer el usuario.

# Tiene la siguiente tarifa:

#     Viaje mínimo $50
#     Si recorre entre 0 y 10km: $20/km
#     Si recorre 10km o más: $15/km

# Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario 
# y muestre el precio del viaje.

def remiseria():
                MIN=50
                km=float(input("Ingrese la cant de km que recorrio: "))
                if km<10:
                    MIN+= km*20
                else:
                    MIN+=15*km
                print("El costo del viaje es de" , MIN)
                    
remiseria()