edad = int(input("Ingrese edad:"))
estatura = float(input("Ingrese estatura:"))

if(edad >= 10 and estatura > 1.60):
    print("¡Puede acceder!")
else:
    print("No es posible acceder")
    if(edad<10):
        print("Lo siento, eres demasiado joven para acceder.")
    else:
        print("Lo siento, eres demasiado bajo para acceder")