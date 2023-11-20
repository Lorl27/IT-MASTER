"""
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin del estante), se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.
"""


def main():
    # ANTES DE LOS ESTANTES
    tot_i = 0
    tot_h = 0
    tot_n = 0
    estante = input("Estante: ").upper()
    while estante != 'F':
        # DURANTE UN ESTANTE
        # ANTES DE UN LIBRO
        max_cant_p = -float('inf')
        nombre_libro = input("Nombre libro: ").upper()        
        while nombre_libro != 'FIN':
            cant_p = int(input("Cantidad de p.:"))

            genero = input("Genero: ").upper()
            while genero not in ('N','I','H'):
                print(f"Error ==> {genero} No es valido!! ")
                genero = input("Genero: ").upper()
            
            
            if genero == 'I':
                tot_i += 1
            elif genero == 'H':
                tot_h += 1
            else:
                tot_n += 1 
            # PARA CADA LIBRO DE CADA ESTANTE
            if cant_p > max_cant_p:
                max_cant_p = cant_p
                nombre_maximo = nombre_libro
            nombre_libro = input("Nombre libro: ")
        # FIN DE LOS LIBROS DE UN ESTANTE
        print(f"El libro del estante {estante} con mas p. es: {nombre_maximo}")
        estante = input("Estante: ")
    # DESPUES DE LOS ESTANATES    
    print(f"Genero I: {tot_i}")
    print(f"Genero H: {tot_h}")
    print(f"Genero N: {tot_n}")
    




main()

