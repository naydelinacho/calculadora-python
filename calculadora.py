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
    print(" 5. Potencia")
    print(" 6. Módulo")
    print(" 7. Raíz cuadrada")
    print(" 8. Porcentaje")
    print(" 9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
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
            elif opcion == "5":
                base = leer_numero("Base: ")
                exponente = leer_numero("Exponente: ")
                resultado = op.potencia(base, exponente)
            elif opcion == "6":
                a = leer_numero("Dividendo: ")
                b = leer_numero("Divisor: ")
                resultado = op.modulo(a, b)
            elif opcion == "7":
                n = leer_numero("Número: ")
                resultado = op.raiz_cuadrada(n)
            elif opcion == "8":
                porc = leer_numero("Porcentaje (por ejemplo 15): ")
                cantidad = leer_numero("Cantidad: ")
                resultado = op.porcentaje(porc, cantidad)
            elif opcion == "9":
                n = leer_numero("Número: ")
                resultado = op.valor_absoluto(n)
            elif opcion == "10":
                n = leer_numero("Número entero (0 o mayor): ")
                resultado = op.factorial(n)
            elif opcion == "11":
                cantidad = leer_numero("¿Cuántos números vas a ingresar? ")
                if cantidad < 1 or cantidad != int(cantidad):
                    raise ValueError("La cantidad debe ser un entero mayor a cero.")
                numeros = []
                for i in range(int(cantidad)):
                    numeros.append(leer_numero(f"Número {i + 1}: "))
                resultado = op.promedio(numeros)
            elif opcion == "12":
                n = leer_numero("Número a redondear: ")
                decimales = leer_numero("Cantidad de decimales: ")
                resultado = op.redondear(n, decimales)
            else:
                print("Opción inválida. Elige una opción del menú.")
                continue

            print(f"Resultado: {resultado}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()