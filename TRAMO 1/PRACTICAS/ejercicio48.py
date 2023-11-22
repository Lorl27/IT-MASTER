# Escribir un programa que permita realizar varias operaciones matemáticas 
# ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y
# dos números enteros en el caso que no haya elegido ‘F’.
# La computadora debe mostrar el resultado para la operación ingresada. 
# Considerar que no se puede dividir por cero.
# Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.

def main():
    
    while True:
        operacion=input("Indique la operacion A realizar: \n +,-,*,/ \n F->finalizar \n").strip() #x si ponen espacios
        
        if (operacion.upper()=='F'):
            break
        else:
            print("Ingrese 2 numeros enteros: ")
            a=input("nro 1: ")
            b=input("Nro 2: ")
            
        try:
            a=int(a)
            b=int(b)
            
            if operacion=='+':
                print("resultado=", a+b)
            elif operacion=='-':
                print ("resultado=",a-b)
            elif operacion=='*':
                print("resultado=",a*b)
            elif operacion=='/':
                try:
                    print("resultado=",a/b)
                except ZeroDivisionError:
                    print("NO se puede dividir por cero!") 
            else:
                print("Ha ocurrido un error. Asegurate de ingresar bien la operacion")
            
        except ValueError:
            print("Tipo ingresado NO es entero")
            pass
        
            
            
if __name__=="__main__":
    main()