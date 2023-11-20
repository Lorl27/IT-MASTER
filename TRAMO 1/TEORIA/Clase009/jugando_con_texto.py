
from sys import path
path.insert(0,'recursos/')
from datos import TEXTO

def limpiar_palabras(lista_palabra:list[str])->list[str]:
    lista = []

    for palabra in lista_palabra:
        nueva=''
        for letra in palabra:
            if letra.isalnum():
                nueva+=letra
        lista.append(nueva)
    return lista

def buscar_secuencia(lista_palabras:list,palabra:str)->int|None:
    for index,dato in enumerate(lista_palabras):
        if dato[0] == palabra:
            return index
    return None    

def  obtener_contadores(palabras:list[str])->list:
    lista = []

    for palabra in palabras:
        pos = buscar_secuencia(lista,palabra)
        if pos:
            lista[pos][1]+=1
        else:
            lista.append([palabra,1])
    return lista


def main():
    texto = TEXTO[:]
    
    # print(len(list(set(limpiar_palabras(TEXTO[:].lower().split())))))
    
    
    
    #lista_palabras = list(set(limpiar_palabras(texto.lower().split())))

    #print(lista_palabras)
    #print(len(lista_palabras))

    lista = limpiar_palabras(texto.lower().split())
    lista_contadores = obtener_contadores(lista)
    for palabra,contador in lista_contadores:
        print(f"{palabra} ==> {contador}")
main()


