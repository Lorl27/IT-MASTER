#Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y
# muestre por pantalla un mensaje que indique cuántos años tendrá la persona después de
# sumarle a su edad la cantidad de años ingresada. El mensaje
# debe tener el siguiente formato:
# 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'"

name=input("Ingrese su nombre: ")
edad=int(input("ingrese su edad: "))
cantA= int(input("Ingrese una cantidad de años: "))

print(f"Hola {name}. Dentro de {cantA} tendrás {(edad + cantA)} años.")