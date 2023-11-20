#Escribir un programa que muestre todos los números enteros del 1 al 5,
# y luego los mismos números pero en orden inverso.

def main():
    ordenados()
    inversos()
    

def ordenados():
    for x in range(1,6):
        print(x)

def inversos():
    contador=5
    while contador!=0:
        print(contador)
        contador-=1
        
if __name__ == "__main__":
    main()