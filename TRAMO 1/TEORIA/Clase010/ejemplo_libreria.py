from sys import path
path.insert(0,'recursos/')
from datos import ARTICULOS_LIBRERIA


def crear_dicc_articulos(articulos:list)->dict[str,dict]:
    lista_titulos = ['codigo','nombre','precio']
    dic = {}
    for t in articulos:
        x = dict(zip(lista_titulos,t))
        dic[x['codigo']] = x

    return dic

def main():
    dic_articulos = crear_dicc_articulos(ARTICULOS_LIBRERIA.copy())    
    for clave,valor in dic_articulos.items():
        print(f"{clave:5} {valor['nombre']:25} {valor['precio']:8.2f}")

main()

