# Calculadora en Python

## Descripción

Calculadora de consola desarrollada en Python como parte de la Práctica 2 de SIS2420 (Actualización tecnológica). Permite realizar operaciones matemáticas desde un menú, valida las entradas del usuario, evita errores como la división entre cero y guarda un historial de las operaciones de la sesión.

El proyecto está dividido en dos archivos:

- `calculadora.py`: menú, lectura de datos, resultados e historial.
- `operaciones.py`: funciones matemáticas.

## Operaciones y estado

| N.º | Funcionalidad | Estado |
|-----|---------------|--------|
| 1 | Potencia | ✅ Completada |
| 2 | Módulo | ✅ Completada |
| 3 | Raíz cuadrada | ✅ Completada |
| 4 | Porcentaje | ✅ Completada |
| 5 | Valor absoluto | ✅ Completada |
| 6 | Factorial | ✅ Completada |
| 7 | Promedio | ✅ Completada |
| 8 | Redondeo | ✅ Completada |
| 9 | Validación de entradas | ✅ Completada |
| 10 | División por cero | ✅ Completada |
| 11 | Mejorar el menú | ✅ Completada |
| 12 | Repetir operaciones | ✅ Completada |
| 13 | Historial de operaciones | ✅ Completada |
| 14 | Limpiar historial | ✅ Completada |
| 15 | Mejorar documentación | ✅ Completada |

Además de estas funcionalidades, el programa incluye suma, resta, multiplicación y división.

## Tecnologías

- Python 3
- Git
- GitHub (Issues)
- Markdown

## Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/naydelinacho/calculadora-python.git
   ```

2. Entra a la carpeta del proyecto:

   ```bash
   cd calculadora-python
   ```

3. Ejecuta el programa (requiere Python 3 instalado):

   ```bash
   python calculadora.py
   ```

## Ejemplos de uso

### Porcentaje

```text
Elige una opción: 8
Porcentaje (por ejemplo 15): 15
Cantidad: 200
Resultado: 30.0
```

### División entre cero

```text
Elige una opción: 4
Dividendo: 5
Divisor: 0
Error: No se puede dividir entre cero.
```

### Entrada no numérica

```text
Elige una opción: 1
Primer número: abc
Entrada no válida. Ingresa un número.
Primer número: 4
```

### Promedio

```text
Elige una opción: 11
¿Cuántos números vas a ingresar? 3
Número 1: 2
Número 2: 4
Número 3: 6
Resultado: 4.0
```

### Historial

```text
Elige una opción: 13

--- Historial de operaciones ---
1. 15.0% de 200.0 = 30.0
2. promedio de [2.0, 4.0, 6.0] = 4.0
```

## Autor
NAYDELIN JHANEYDI ACHO MAMANI