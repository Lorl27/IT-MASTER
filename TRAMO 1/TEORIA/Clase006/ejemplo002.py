

def calcular_factorial(numero):    
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def es_primo(numero):
    for divisor in range(2,numero):
        if numero%divisor == 0:
            return False
    return True

def main():
    """
    for x in range(1,26):
        print(f"Factorial de {x} es {calcular_factorial(x)}")
    """
    for x in range(1,1000):
        if es_primo(x):
            print(f"Factorial de {x} tiena {len(str(calcular_factorial(x)))} digitos")



main()











