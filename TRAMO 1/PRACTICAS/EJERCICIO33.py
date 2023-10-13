# La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra
# con la siguiente escala:

#     Menor de $5500.0 el descuento es del 4.5%
#     Entre $5500.0 y $10000.0 el descuento es del 8%
#     Más de $10000.0 el descuento es del 10.5%

# Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar,
# con mensajes aclaratorios.

def sindical():
    D1 = 4.5 / 100
    D2 = 8 / 100
    D3 = 10.5 / 100
    compra=float(input("Ingrese MONTO compra: "))
    info= f"Usted gasto {compra} pesos "
    if compra<5500:
        coste= compra*D1
        info+= f"Y se le hace un descuento de {coste:.2f}$, TOTAL= {compra-coste:.2f}"
    elif compra<10000:
        coste= compra*D2
        info+= f"Y se le hace un descuento de {coste:.2f}$, TOTAL= {compra-coste:.2f}"
    else:
        coste= compra*D3
        info+= f"Y se le hace un descuetno de {coste:.2f}$, TOTAL= {compra-coste:.2f}"
    print(info)
    
sindical()