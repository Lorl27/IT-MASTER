# Escribir un programa que permita validar una opción ingresada.
# Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar?[S/N]".
# # Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). 
# La opción debe ser ingresada 
# tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.

def main():
    usu=input("¿Deseas continuar? [S/N]").strip().upper()
    
    while usu!='S' and usu!='N':
        print("Dato invalido")
        usu=input("¿Deseas continuar? [S/N]").strip().upper()
        
    print(f"has elegido: {usu}")
    
if __name__=="__main__":
    main()