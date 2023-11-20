import sys
sys.path.append('recursos/')
import funciones as fun 
from fechas_int import es_fecha_valida





def main():
    
    # numero = fun.leer_entero_entre("Ingrese un valor entero: ",1,10)
    for cadena in sys.path:
        print(cadena)
    numero = fun.leer_entero("Ingrese una fecha (AAAAMMDD): ")
    while not es_fecha_valida(numero):
        print(f"La fecha: {numero} no es un fecha!")
        numero = fun.leer_entero("Ingrese una fecha (AAAAMMDD): ")


main()

