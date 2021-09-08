def main():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Sumatoria")
    value = int(input("Seleccione la opción deseada: "))
    
    if value == 1:
        resultado = sumar_menu()
        print("El resultado de la suma es: " + str(resultado))
    elif value == 2:
        restar_menu()
    elif value == 3:
        dividir_menu()
    elif value == 4:
        multiplicar_menu()
    else:
        resultado = sumatoria_menu()
        print("El resultado de la sumatoria es: " + str(resultado))


def sumar_menu():
    print("Menu sumar")
    num = int(input("Ingrese el primer sumando: "))
    num2 = int(input("Ingrese el segundo sumando: "))
    return sumar(num, num2)

def sumar(a, b):
    return a + b


def restar_menu():
    print("Menu restar")
    num = int(input("Ingrese el minuendo: "))
    num2 = int(input("Ingrese el sustraendo: "))
    return restar(num, num2)

def restar(a, b):
    return a - b


def multiplicar_menu():
    print("Menu multiplicar")
    num = int(input("Ingrese el multiplicando: "))
    num2 = int(input("Ingrese el multiplicador: "))
    return multiplicar(num, num2)

def multiplicar(a, b):
    return a * b


def dividir_menu():
    print("Menu dividir")
    num = int(input("Ingrese el dividendo: "))
    num2 = int(input("Ingrese el divisor: "))
    return dividir(num, num2)

def dividir(a, b):
    return a / b


def sumatoria_menu():
    print("Menu sumatoria")
    num = int(input("Ingrese un total de numeros: "))
    lista_numeros = list(range(0, num))

    return sumatoria(lista_numeros)

def sumatoria(lista_numeros):
    return sum(lista_numeros)


if __name__ == "__main__":
    main()