#Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
# Verificar que el mes sea válido e informar en caso que no lo sea.

def mes():
    mes=int(input("Dame un numero de mes: "))
    letra=input("Escribelo en letras: ")
    if "mayo"!=letra and mes!=5 or "enero"!=letra and mes!=1 or "febrero"!=letra and mes!=2 or "marzo"!=letra and mes!=3 or "abril"!=letra and mes!=4 or "junio"!=letra and mes!=6 or "julio"!=letra and mes!=7 or "agosto"!=letra and mes!=8 or "septiembre"!=letra and mes!=9 or "octubre"!=letra and mes!=10 or "noviembre"!=letra and mes!=11  or "diciembre"!=letra and mes!=12:
        print("No es valido")
    else:
        print("Es valido")
        
mes()