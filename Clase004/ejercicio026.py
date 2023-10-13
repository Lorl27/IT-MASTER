"""
ej 26


invitados = int(input("Ingrese cantidad de invitados: "))
asientos = int(input("Ingrese cantidad de asientos disponibles: "))
if asientos >= invitados:
  cartel = "Tienes suficientes asientos para los invitados."
else:
  asientos_faltantes = invitados - asientos
  cartel = f"Faltan {asientos_faltantes} asientos para los invitados."
print(cartel)

"""
invitados = int(input("Ingrese el numero de invitados: "))
ASIENTOS = 44

if invitados <= ASIENTOS:
    print("entran todos")
else:
    print("Los invitados no entran.")
    print(f"Faltan {invitados - ASIENTOS} asientos.")