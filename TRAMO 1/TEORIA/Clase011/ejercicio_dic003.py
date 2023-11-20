"""
Crea un diccionario donde las llaves sean las diferentes categorías de productos ("ref" para refrigerados, "alm" para alimentos no refrigerados, "lim" para limpieza, "per" para productos personales), y los valores sean listas de los nombres de los productos en esa categoría.

nombre => 'pdental'
categoria => 'per'

dic = {
    "ref":[
        "kweldjflks",
        "ksjkl"
    ],
    "lim":[
        "jahjkas",
        "jkdhjk"
    ]
}

"""

import sys

sys.path.insert(0,'recursos/')

import datos

def obtener_dic(lista):
    dic = {}
    # ("2001", "Leche", 1.20, "ref")
    for _, nombre, _, categoria in lista: 
        if categoria in dic.keys():
            dic[categoria].append(nombre)
        else:
            dic[categoria] = [nombre]


    return dic

def main():
    lista_productos = datos.ARTICULOS_ALMACEN[:]
    dic = obtener_dic(lista_productos)
    for cat,lista_nombres in dic.items():
        print(f"Categoria: {cat}")
        for nombre in lista_nombres:
            print(f"--{nombre}")
    print("-"*100)
    for cat in dic.keys():
        print(f"Categoria: {cat}")
        for nombre in dic[cat]:
            print(f"--  {nombre}")


main()
