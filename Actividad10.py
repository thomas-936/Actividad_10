print("Actividad 10")

opcion = 0

def suma_naturales(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        suma = 0
        for i in range(n, 1, -1):
            suma += i


while opcion != 6:
    print("+++MENU RETOS RECURSIVOS+++")
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


        case 2:
            print("Calcular la suma de los primeros N números naturales")
            num = int(input("Ingrese un número natural: "))
            print(f"\nLa suma de los números naturales hasta {num} es {suma_naturales(num)}")