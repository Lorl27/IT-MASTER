# Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e 
# indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10,
# debe informar un error.

#     Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#     Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#     Se debe recuperar cuando al menos una de las dos notas es menor a 4.

def alumno():
    nota1=float(input("NOTA 1: "))
    nota2=float(input("NOTA 2: "))
    while nota1 in range(1,11) and nota2 in range(1,11):
        if nota1>=7 and nota2>=7:
            print("PROMOVIDO")
            break
        elif nota1>=4 and nota2>=4:
            print("APROBADO")
            break
        else:
            print("RECURSA")
            break
        
alumno()