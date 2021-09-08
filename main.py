def main():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    value = int(input("Selecciona la operacion a realizar: "))
    print("La opción que selecciono es: " + str(value))

    if value == 1:
        resultado = menu_sumar()
        print("El resultado de la suma es: " + str(resultado))
    if value == 3:
        resultado = menu_multiplicar()
        print("El resultado de la multiplicación es: " + str(resultado))

def menu_sumar():
    print("Menu sumar")
    num = int(input("Ingrese el primer sumando: "))
    num2 = int(input("Ingrese el segundo sumando: "))
    return sumar(num, num2)

def sumar(a, b):
    return a + b

def menu_multiplicar():
    print("Menu multiplicar")
    num = int(input("Ingrese el primer factor: "))
    num2 = int(input("Ingrese el segundo factor: "))
    return multiplicar(num, num2)

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    main()