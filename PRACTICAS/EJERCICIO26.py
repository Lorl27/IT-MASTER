#Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y 
# la cantidad de asientos disponibles en el salon.
# Debes indicar si alcanzan los asientos, 
# Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.

def invitados_asientos():
    invitados=int(input("Ingresá la cantidad de invitados: "))
    asientosD=int(input("Ingresá la cantidad de asientos disponibles: "))
    faltan=  invitados - asientosD
    if invitados<=asientosD :
        print("Todos los asientos alcanzan")
    else:
        print(f"Faltan {faltan} asientos")


invitados_asientos()