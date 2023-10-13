edad = int(input('Ingrese su edad: '))
estatura = float(input('Ingrese su estatura en cm: '))

if edad >=10 and estatura > 160:
    print('Puede entrar')
elif edad < 10:
    print('No puede ingresar alguien tan joven')
elif estatura < 160 :
    print('No puede ingresar alguien tan bajo')
elif edad < 10 and estatura <= 160:
    print('Ustede es muy joven y su estauta no coincide con el minimo')