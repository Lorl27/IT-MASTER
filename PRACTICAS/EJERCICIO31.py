# Una editorial determina el precio de un libro según la cantidad de páginas que contiene.
# El costo básico del libro es de $1000, más $35,10 por página con encuadernación rústica. 
# Si el número de páginas supera las 300 la encuadernación debe ser especial, 
# lo que incrementa el costo en $1200. 
# Además, si el número de páginas sobrepasa las 600 se hace necesario otro procedimiento de encuadernación 
# que incrementa el costo en $880. 
# Desarrollar un programa que calcule el costo de un libro dado el número de páginas.

# En Python no existen constantes como tal, pero se utiliza una convención de nomenclatura en mayúsculas 
# para indicar que una variable no debe ser modificada. 
# Esto se conoce como "constante simbólica" o "constante convencional".
# Para definir una constante convencional, simplemente se define una variable con un nombre en mayúsculas.

# Por ejemplo, para el problema anterior, se pueden definir las constantes:

# COSTO_BASICO con valor 1000

# COSTO_POR_PAGINA con valor 35.10

# COSTO_ENC_RUSTICA con valor 1200

# COSTO_ENC_ESPECIAL con valor 880.

def libreria():
    COSTO_BASICO = 1000
    COSTO_POR_PAG = 35.10
    COSTO_EN_RUSTI=1200
    COSTO_ENC_ESP=880
    num_pags= int(input("Ingrese el numero de paginas: "))
    costo=COSTO_BASICO + COSTO_POR_PAG*num_pags
    if num_pags<=300:
        costo=costo
    elif num_pags <=600:
        costo*= COSTO_EN_RUSTI
    else:
        costo*= COSTO_ENC_ESP
    print(f"Tu libro saldá {costo}$")
    
libreria()