from operator import invert

print("Actividad 10")

opcion = 0

def suma_naturales(n):
    if n == 0:
        return 0

    else:
        return n + (suma_naturales(n-1))

def inversor (cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return  inversor(cadena[1: ])+ cadena[0]
def cuenta_regresiva(n):
    if n == 1:
        return 1
    else:
        return n, cuenta_regresiva(n-1)


while opcion != 6:
    print("\n+++MENU RETOS RECURSIVOS+++")
    print("1. Invertir una cadena de texto")
    print("2. Calcular la suma de los primeros N números naturales")
    print("3. Imprimir una cuenta regresiva desde N hasta 1")
    print("4. Sumar los dígitos de un número")
    print("5. Contar cuántos dígitos tiene un número")
    print("6. Salir... ")
    try:
        opcion = int(input("Ingrese su opción: "))
    except ValueError:
        print("\nIngreso no valido")
        continue

    match opcion:
        case 1:
            print("Invertir una cadena de texto")
            cadena  = input("Ingrese un string: ")
            print(f"El string invertido es: {inversor(cadena)}")

        case 2:
            print("Calcular la suma de los primeros N números naturales")
            num = int(input("Ingrese un número natural: "))
            print(f"\nLa suma de los números naturales hasta {num} es {suma_naturales(num)}")

        case 3:
            print("Cuenta regresiva... ")
            numero = int(input("Ingrse un núemero n: "))
            print(f"La cuenta regresiva es: {cuenta_regresiva(numero)}")

