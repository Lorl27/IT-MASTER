"""
Ejercicio 065
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. 

Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.

Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
3) Hamburguesa sola - 1300
4) Hamburguesa con queso - 1400
5) Gaseosa - 700
6) Postre - 600
7) Agregar aderezo - 100
8) Terminar

Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.

El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.

Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".
"""

from sys import path
path.insert(0,'recursos/')
import funciones as fun



TERMINAR = 8
PRECIOS = (4000.0,4500.0,1500.0,2000.0,1000.0,850.0,250.0)
#index        0     1      2      3      4       5    6


OPCIONES_MENU = f"""
Comidas Carlitos;
{'Combo 1: Hamburguesa, papas fritas y gaseosa':70}{PRECIOS[0]:10.2f};
{'Combo 2: Hamburguesa con queso, papas fritas y gaseosa':70}{PRECIOS[1]:10.2f};
{'Hamburguesa sola':70}{PRECIOS[2]:10.2f};
{'Hamburguesa con queso':70}{PRECIOS[3]:10.2f};
{'Gaseosa':70}{PRECIOS[4]:10.2f};
{'Postre':70}{PRECIOS[5]:10.2f};
{'Agregar aderezo':70}{PRECIOS[6]:10.2f}"""

def main():

    opcion = fun.menu(OPCIONES_MENU)
    while opcion != TERMINAR:
        if opcion == 1:
            pass # subtotal += proc_opcion(PRECIOS[opcion-1])
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        opcion = fun.menu(OPCIONES_MENU)

main()
