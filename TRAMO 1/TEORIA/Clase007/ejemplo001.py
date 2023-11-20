from random import randint



def generar_lista(cantidad_elementos:int,numero_desde:int,numero_hasta:int)->list[int]:
    lista = []
    for x in range(cantidad_elementos):
        lista.append(randint(numero_desde,numero_hasta))
    return lista


def eliminar_elemento(lista:list[int],valor_eliminar:int):
    for index, valor  in enumerate(lista):
        if valor == valor_eliminar:
            lista.pop(index)

def eliminar_elementos(lista:list,valores_eliminar:tuple):
    for index, valor  in enumerate(lista):
        if valor in valores_eliminar:
            lista.pop(index)



def main():
    lista = generar_lista(10,1,10)
    print(lista)
    eliminar_elementos(lista,(1,2,8))
    print(lista)

main()

