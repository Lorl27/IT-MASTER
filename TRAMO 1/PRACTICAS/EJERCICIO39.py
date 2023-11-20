# Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176

def main():
    x=42
    y=176
    suma=0
    
    for i in range(x, y + 1):
        suma += i
        print(suma)
        
    print("La suma de los números entre 42 y 176 es:", suma)
        
    #  while (x <= y):
    #     suma+=x
    #     x+=1
    
if __name__ == "__main__":
    main()