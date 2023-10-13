# Escribir un programa que permita resolver el siguiente problema:

# Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y
# qué porcentaje aportó cada una (indicando nombre y porcentaje).

# Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto 
# calcular e informar lo requerido previamente.

def capSoci():
    socio1=input("Ingresá el nombre del primer socio: ")
    s1CAP=float(input("Ingresa el monto aportado: "))
    socio2=input("Ingresá el nombre del 2do socio: ")
    s2CAP=float(input("Ingresa el monto aportado: "))
    socio3=input("Ingresá el nombre del tercer socio: ")
    s3CAP=float(input("Ingresa el monto aportado: "))
    
    total= s1CAP+s2CAP+s3CAP
    
    i1=round((s1CAP/total)*100)
    i2=round((s2CAP/total)*100)
    i3=round((s3CAP/total)*100)
    print(f"El total invertido es de: {total}. {socio1} aportó {i1}%, {socio2} aport {i2}% y {socio3} aporto {i3}%")
    
capSoci()