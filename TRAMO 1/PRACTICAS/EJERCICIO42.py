# Escribir un programa que lea números enteros hasta que se ingrese un 0,
# y muestre el promedio de los números ingresados.

def main():
    n=int(input("Ingrese un numero aca: "))
    suma=0
    contador=0

    while(n!=0):
        suma+=n
        contador+=1
        n=int(input("Ingrese un numero aca: "))
    promedio=suma/contador
    print(f"promedio de los {contador} numeros, cuya suma es {suma}; {promedio}")
    return 0

if __name__=="__main__":
    main()