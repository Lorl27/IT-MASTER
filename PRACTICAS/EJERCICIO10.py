#Escribir un programa para resolver el siguiente problema:

#Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales).
# Calcular qué porcentaje invirtió cada una.

perso1=float(input("p1: "))
perso2=float(input("p2: "))
perso3=float(input("p3: "))

total= perso1 +perso2  + perso3

inversion1 = round((perso1/total) * 100) #el 100 para el porcentaje
inversion2 = round((perso2/total) * 100)
inversion3 = round((perso3/total) * 100)
print(f"p1 invirtio {inversion1}% ,p2 {inversion2}% y p3 {inversion3}%")