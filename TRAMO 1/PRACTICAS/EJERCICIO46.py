# Escribir un programa que a partir de un número entero cant ingresado por el usuario 
# permita cargar por teclado cant números enteros. 
# La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

def main():
    l=[]
    n=int(input("Ingrese un numero here: "))
    max=0
    
    while(n!=0):
        x=int(input("Ingrese un numero: "))
        l.append(x)
        
        if x>max:
            max=x
            
        n-=1
    
    print(f"los nros ingresados fueron: {l}, el maximo es {max} y su posicion es {l.index(max)}")
    
if __name__=="__main__":
    main()