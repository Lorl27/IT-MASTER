# Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.

# La computadora debe mostrar el número máximo y el número mínimo


def main():
    l = []
    max = float("-inf")
    min = float("inf")

    number = int(input("Ingrese un nro. 0 para finalizar"))
    while number != 0:
        l.append(number)
        if number > max:
            max = number
        if number < min:
            min = number
        number = int(input("Ingrese un nro. 0 para finalizar"))

    print(f"has ingresado {l} numeros, el mayor es {max} y el menor {min}")


if __name__ == "__main__":
    main()
