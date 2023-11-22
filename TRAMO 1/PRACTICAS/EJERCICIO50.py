# Escribir un programa que permita validar la nota de un examen. 
# Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.

# La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida
# dentro del rango indicado.

#     Las notas 1 y 3 no usan nunca.
#     La nota 0 se reserva para los ausentes.

# Las notas válidas pueden ser un 2 o un valor entre 4 y 10.

def main():
    while True:
        nota=input("Ingrese una nota en el rango [0..10]")
        try:
            nota=int(nota)
            if nota==2 or 4<=nota<=10:
                print(nota)
                break
            else:
                print("NOTA FUERA DEL RANGO!")
        except ValueError:
            print("NOTA INVALIDA")
            
if __name__=="__main__":
    main()