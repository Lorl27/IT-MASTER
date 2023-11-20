# Escribir un programa que permita leer dos números naturales A y B. 
# Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.

# Ejemplo:

#     4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
#     3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces)

def main():
    a=int(input("Ingrese un nro: "))
    b=int(input("Ingrese otro nro: "))
    
    copia=b
    resultado=1
    while(b>0):
        resultado*=a
        b-=1
        
    print(f"{a} elevado a {copia}=={resultado}")
    
if __name__=="__main__":
    main()