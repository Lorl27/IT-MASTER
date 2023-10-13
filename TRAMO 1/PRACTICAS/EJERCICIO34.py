# Escribir un programa que calcule y muestre el sueldo neto de un empleado en base 
# a su sueldo básico y su antigüedad en años. 
# Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, 
# mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad.
# También se le realizan los siguientes descuentos:

#     Jubilación: 11%

#     Obra Social: 3%

#     Sindicato: 3%

# Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil 
# (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)

# Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

# Descuentos:

#     Jubilación - 999,99

#     Obra Social - 999,99

#     Sindicato - 999,99

# Sueldo Neto 999,99

def empleadito():
    JUBILACION= 11 / 100
    OBRA_SOCIAL,SINDICATO=3 / 100 , 3/100
    SOLTERO, CASADO = 5/100 , 7/100
    sueldo_basico=float(input("INGRESE EL SUELO BASICO: "))
    antiguedad= float(input("INGRESE LA CANTIDAD DE AÑOS QUE HA ESTADO TRABAJANDO: "))
    estado_civil= input("""INGRESE SU ESTADO CIVIL: 
                        S => SOLTERO
                        C => CASADO""")
    cartel=f"""
                ESTADO CIVIL = {estado_civil}
                SUELDO BASICO = {sueldo_basico}
                ANTIGUEDAD = {antiguedad}
                
                DESCUENTOS:
                JUBILACION = {sueldo_basico - JUBILACION}
                OBRA SOCIAL= {sueldo_basico - OBRA_SOCIAL}
                SINDICATO= {sueldo_basico -SINDICATO}
            """
    if estado_civil == "S" or estado_civil =="s":
        plata= SOLTERO*antiguedad + sueldo_basico
        cartel+=f"PESO NETO: {plata}" 
    elif estado_civil == "C" or estado_civil =="c":
        plata= CASADO*antiguedad + sueldo_basico
        cartel+=f"PESO NETO: {plata}" 
    else:
        print("VALOR ERRONEO")
    print(cartel)

empleadito()   