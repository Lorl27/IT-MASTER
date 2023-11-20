# Escribir un programa que permita ingresar un número entero n. 
# Debe mostrar los primeros 10 múltiplos de n.

# Ejemplo:

# n = 5  

# n x 1 = 5  
# n x 2 = 10  
# n x 3 = 15  
# n x 4 = 20  
# n x 5 = 25  
# n x 6 = 30  
# n x 7 = 35  
# n x 8 = 40  
# n x 9 = 45  
# n x 10 = 50   

def main():
    n= int(input("Introduzca un numero: "))
    contador=1
    while(contador<=10):
        m=n*contador
        print(f"{n}*{contador}=={m}")
        contador+=1
        

if __name__ == "__main__":
    main()
# end main
