# Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100,
# y muestre la cantidad de números ingresados.

def main():
    
    suma=0
    cant=0
    
    while(suma<=100):
        n=int(input("ingresa un nro: "))
        suma+=n
        cant+=1
        
        
    print(f"la cantidad de nros ingresados fue {cant}, suma={suma}")
    return 0

if __name__=="__main__":
    main()