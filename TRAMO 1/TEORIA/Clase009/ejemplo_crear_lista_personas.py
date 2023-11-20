


"""
Ejercicio 053
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.
"""

from sys import path
path.insert(0,'recursos/')
from datos import obtener_nombre_completo
from random import randint

def crear_personas(cantidad_personas:int)->list:
    lista = []

    for x in range(cantidad_personas):
        nombre = obtener_nombre_completo()
        edad = randint(18,75)
        lista.append((nombre,edad))

    return lista


def orden_por_edad(tupla:tuple)->int:
    return tupla[1]

def limpia(cadena:str)->str:
    sin_tilde = "aeiouAEIOU"
    con_tilde = "áéíóúÁÉÍÓÚ"
    nueva = ''
    for letra in cadena:
        if letra in con_tilde:            
            nueva += sin_tilde[con_tilde.index(letra)]
        else:
            nueva += letra
    return nueva

def orden_por_nombre(tupla:tuple)->str:
    return limpia(tupla[0])

def orden_loco(tupla:tuple)->int:
    return len(tupla[0]) + tupla[1]

def filtrar_iguales(personas:list,edad_buscada:int)->list:
    lista = []
    for nombre,edad in personas:
        if edad == edad_buscada:
            lista.append((nombre,edad))
    return lista

def main():
    
    personas = crear_personas(10000)    
    menores = filtrar_iguales(personas,min(personas,key=orden_por_edad)[1])
    for x in menores:
        print(x)
"""    personas.sort(key=orden_por_edad)
    print(f"{personas[0][0][:30]:30} {personas[0][1]:6}")
"""    """for nombre,edad in personas:
        print(f"{nombre[:30]:30} {edad:6}")
"""

main()



