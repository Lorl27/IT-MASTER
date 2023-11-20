"""
Invierte las llaves y los valores del diccionario que contiene los cuadrados, de tal manera que los cuadrados sean las llaves y los números originales sean los valores.
"""

def main():
    dic = { x:x**2 for x in range(1,6)  }
    otro_dic = { v:k for k,v in dic.items()}
    # otro_dic ==> {1:1,2:4}.items() ==> [(1,1),(2,4)]
    otro_dicc = {x**2 : x for x in range(1,6)}
    print(dic)
    print(otro_dic)
    print(otro_dicc)
main()