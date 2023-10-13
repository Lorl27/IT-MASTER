#Existen dos reglas que identifican dos conjuntos de valores:

#     a) El número es de un solo dígito.
#     b) El número es impar.

# A partir de estas reglas, escribir un programa que permita ingresar un número entero.

# Debe asignar el valor que corresponda a las variables booleanas:

#     esDeUnSoloDigito
#     esImpar
#     estaEnAmbos
#     noEstaEnNinguno

# el valor Verdadero o Falso, según corresponda, para indicar si 
# el valor número ingresado pertenece o no a cada conjunto.
# Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.

def algo(x):
    esDeUnSoloDigito= False
    esImpar=False
    estaEnAmbos=False
    noEstaEnNinguno=False
    largo = str(x)
    if len(largo) == 1 and x%2==1:
        estaEnAmbos=True
    elif len(largo) == 1:
        esDeUnSoloDigito=True
    elif x%2==1:
        esImpar=True
    else:
        noEstaEnNinguno=True
    print(f"""{x}:
            IMPAR: {esImpar}
            1 DIGITO: {esDeUnSoloDigito}
            AMBOS:{estaEnAmbos}
            NINGUNO:{noEstaEnNinguno}""")
algo(5)
algo(2)
algo(10)
algo(11)