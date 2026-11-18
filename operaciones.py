import math


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

 
def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("0 elevado a un exponente negativo no está definido.")
    return base ** exponente


def modulo(a, b):
    if b == 0:
        raise ValueError("El divisor del módulo no puede ser cero.")
    return a % b   
    

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No existe la raíz cuadrada de un número negativo.")
    return math.sqrt(n)


def porcentaje(porc, cantidad):
    return cantidad * porc / 100


def valor_absoluto(n):
    return abs(n)