nota1 = int(input("Ingrese nota 1"))
nota2 = int(input("Ingrese nota 2"))

error_de_datos = (nota1 < 0 and nota1 > 10) or (nota2 < 0 and nota2 > 10)

aprueba = (nota1 >= 4 and nota2 >= 4) and (nota1 < 7 and nota2 < 7)
desaprueba = nota1 < 4 or nota2 < 4
promociona = (nota1 >= 7 and nota2 >= 7)

if not error_de_datos:
    if aprueba:
        print("Aprueba")
    if desaprueba:
        print("Desaprueba")
    if promociona:
        print("Promociona")
else:
    print("error de datos")