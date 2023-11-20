# Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.

def main():
    n=int(input("Ingrse un numero"))
    max=0
    while(n!=0):
        if n>max:
            max=n
        n=int(input("Ingrse un numero"))
    
    print(max)
    return 0

if __name__ =="__main__":
    main()