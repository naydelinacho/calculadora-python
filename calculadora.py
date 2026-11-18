import operaciones as op


def leer_numero(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


def mostrar_menu():
    print("\n========== CALCULADORA ==========")
    print(" 1. Suma")
    print(" 2. Resta")
    print(" 3. Multiplicación")
    print(" 4. División")
    print(" 0. Salir")
    print("=================================")


def main():
    print("Bienvenido a la calculadora")
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        try:
            if opcion == "1":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                resultado = op.sumar(a, b)
            elif opcion == "2":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                resultado = op.restar(a, b)
            elif opcion == "3":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                resultado = op.multiplicar(a, b)
            elif opcion == "4":
                a = leer_numero("Dividendo: ")
                b = leer_numero("Divisor: ")
                resultado = op.dividir(a, b)
            else:
                print("Opción inválida. Elige una opción del menú.")
                continue

            print(f"Resultado: {resultado}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()