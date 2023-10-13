#Escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
# un género ('F'para mujeres, 'M' para hombres) y un nombre. 
# En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido),
# informar tal situación indicando el nombre de la persona. 
# Si los datos están bien ingresados el programa debe indicar, 
# sabiendo que las mujeres se jubilan con 60 años o más
# y los hombres con 65 años o más, si la persona está en edad de jubilarse.

def jubilado():
    edad=int(input("Ingresa una edad: "))
    genero=input("Ingresa 'F' para femenino o 'M' para masculino (genero): ")
    name=input("Ingresa tu nombre: ")
    if edad>=60 and genero=="F":
        print(f"{name} se puede jubilar!")
    elif edad>=65 and genero=="M":
        print(f"{name} se puede jubilar!")
    elif edad<=0 or edad>120:
        print(F"{name},VALOR INCORRECTO. EDAD FUERA DE RANGO")
    elif edad<60 and genero=="F":
        print(f"{name} no tenes la edad suficiente. CHAU")
    elif edad<65 and genero=="M":
        print(f"{name} no tenes la edad suficiente. CHAU")
    elif genero!="F" or genero!="M":
        print(f"{name} HA INGRESADO UN GENERO NO SOPORTADO POR EL SISTEMA")
    else:
        print(f"{name} NO SE PUEDE JUBILAR.CHAU")
        
jubilado()