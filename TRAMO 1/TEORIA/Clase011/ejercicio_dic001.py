"""
Crea un diccionario en el cual las llaves sean números enteros y los valores sean sus cuadrados. Haz esto para números del 1 al 5.
"""

def main():
    print( { x:x**2 for x in range(1,6)  }   )
    print( tuple( x**2 for x in range(1,6)  )   )
    print( [ x**2 for x in range(1,6) ]   )
    print( ','.join( [ str(x**2) for x in range(1,6) ] )   )

main()