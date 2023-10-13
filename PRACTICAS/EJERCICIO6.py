#Escribir un programa que solicite al usuario ingresar tres notas de un alumno.
# El programa debe mostrar por pantalla
# las notas separadas por comas en un renglón y
# el promedio de las notas en el siguiente renglon

print("Ingrese las notas del alumnx: ")
nota1=int(input("NOTA 1: "))
nota2=int(input("NOTA 2: "))
nota3=int(input("NOTA 3: "))



print(f"NOTAS: {nota1}, {nota2} , {nota3}"  , f"PROMEDIO: {nota1 + nota2 + nota3} " , sep="\n"  )