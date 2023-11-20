
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

def obtener_contadores(palabras:list[str])->dict[str,int]:
    dic = dict.fromkeys(set(palabras),0)
    
    for palabra in palabras:
        dic[palabra] += 1


    return dic
   

def criterio_cantidad(t:tuple)->int:
    palabra,cantidad = t
    return cantidad

def criterio_alfa(t:tuple)->int:
    palabra,cantidad = t
    return palabra

def main():
    texto = TEXTO[:]
    lista = limpiar_palabras(texto.lower().split())
    dic_palabras = obtener_contadores(lista)
    
    for palabra,contador in sorted(dic_palabras.items(),key=criterio_cantidad,reverse=True):
        if contador > 1:            
            print(f"{palabra} ==> {contador}")
main()


