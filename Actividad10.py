print("Actividad 10")

opcion = 0

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
        print("Ingreso no valido")
