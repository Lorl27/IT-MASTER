# Escribir un programa que permita validar la nota de un examen. 
# Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.

# La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida 
# dentro del rango indicado.

def main():
    while True:  #  múltiples intentos
        nota = input("Ingrese nota: ")
        
        try:
            nota = int(nota)
            
            if 0 <= nota <= 10:  
                print(nota)
                break  # Sale del bucle si la nota es válida
            else:
                print("La nota ingresada está fuera del rango [0..10]")
                
        except ValueError:
            print("La nota ingresada no es un número entero")
        
        
if __name__=="__main__":
    main()