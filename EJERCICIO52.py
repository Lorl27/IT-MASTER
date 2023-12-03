# Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales)
# de cada jugador de un equipo de básquet 
# La carga finalizará al ingresar cero.
# Calcular y mostrar la estatura promedio del equipo.

def main():
    estatura=float(input("ingrese la altura"))
    l=[]
    while(estatura!=0):
        l.append(estatura)
        estatura=float(input("ingrese la altura"))
    
    if not estatura:
        return 0
    else:
        cant=len(l)
        
        promedio=sum(l)/cant
        print(f"se han ingresado {cant} jugadores, {l}. el promedio de altura es {promedio}")
    
if __name__=="__main__":
    main()