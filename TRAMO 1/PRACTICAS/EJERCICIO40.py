# Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

#     La suma de los numeros pares entre a y b.
#     El producto de los numeros impares entre a y b.

def main():
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingresa otro numero: "))
    suma=0
    producto=1
    if a<=b:
        for x in range(a,b+1):
            #print(f"numero actual:{x}")
            if x%2==0:
                suma+=x
            else:
                producto*=x
    else:
        for x in range(b,a+1):
            #print(f"numero actual:{x}")
            if x%2==0:
                suma+=x
            else:
                producto*=x
    
        
    print(f"La suma entre {a} y {b} par es: {suma} y su producto (entre impares) es {producto}")
    
if __name__ =="__main__":
    main()