# Definición del problema:
# Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, 
# más el 5% del valor de esas ventas.
# Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

# Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

# ¿Sobran datos? ¿Qué datos sobran?

def inmo():
    salario_b= int(input("SALARIO BASE: "))
    comision=float(input("COMISION POR VENTA: "))
    nombre=input("INGRESA NOMBRE DEL VENDEDOR: ")
    ventas_hechas=int(input("CANTIDAD DE VENTAS HECHAS: "))
    porc=ventas_hechas*0.5
    total= salario_b+comision*ventas_hechas+porc
    print(f"El/la vendedor/a {nombre} ha realizado {ventas_hechas} ventas y cobrara: {total}")
    
inmo()