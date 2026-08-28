# Calculadora matricial

Primera versión del laboratorio **"Estructuras de datos y Algoritmos de
ordenamiento"** (Programación 3, Ingeniería Mecatrónica, UMNG), a partir del
PDF `G2-Prog3-Estructuras de datos (Listas, Matrices), Algoritmos de
ordenamiento (1).pdf` que está en este repositorio.

## ¿Qué pide el laboratorio?

El PDF pide dos programas de consola, hechos con programación orientada a
objetos, **sin usar numpy** (todo con listas de Python):

**Punto 3.1 — Calculadora matricial**
- Suma de matrices
- Producto de matrices
- Inversa de una matriz (debe funcionar para cualquier matriz cuadrada)
- Producto de una matriz por un vector

**Punto 3.2 — Ordenamiento**
- Ordenar una lista de números flotantes aleatorios (la cantidad la pide el
  programa al usuario) usando: burbuja, inserción, selección, mergesort y el
  método `sort()` nativo de Python.

**Reglas de diseño exigidas por el enunciado (sección 4):**
- Un menú principal con submenús por punto; el programa no se cierra al
  terminar una opción, sigue permitiendo elegir otra.
- Una sola clase por archivo, y un archivo aparte para el `main`.
- En el `main` las clases se usan por medio de **objetos**, no con llamados
  estáticos.
- Cada clase tiene un **constructor** que inicializa sus datos.
- Los métodos de la clase no reciben parámetros ni retornan nada: usan el
  estado interno del objeto y guardan el resultado; para entregarlo al main
  se usa un método `get_...()`.

## Estructura del proyecto

```
src/
├── main.py                # Menú principal + submenús. Punto de entrada.
├── calculadora_matriz.py  # Clase CalculadoraMatriz (punto 3.1)
├── ordenador.py           # Clase Ordenador (punto 3.2)
└── utilidades.py          # Funciones sueltas para leer/mostrar datos por consola
```

- **`calculadora_matriz.py`**: el constructor recibe (opcionalmente) las
  matrices/vector iniciales. Los métodos `set_matriz_a`, `set_matriz_b` y
  `set_vector` cargan los datos de entrada. Los métodos de operación
  (`sumar`, `multiplicar`, `invertir`, `multiplicar_por_vector`) no reciben
  parámetros ni retornan: calculan y guardan el resultado en
  `self.resultado`. `get_resultado()` lo entrega al main. `invertir()`
  calcula la inversa por el método de determinante y matriz adjunta
  (`A⁻¹ = 1/det(A) · adj(A)`, donde `adj(A)` es la transpuesta de la
  matriz de cofactores), usando funciones auxiliares privadas
  (`_determinante`, `_menor`, `_matriz_cofactores`, `_transponer`).
  Funciona para matrices cuadradas de cualquier tamaño y detecta matrices
  singulares (determinante = 0).
- **`ordenador.py`**: mismo patrón. `set_datos` carga la lista, cada método
  de ordenamiento (`burbuja`, `insercion`, `seleccion`, `mergesort`,
  `sort_python`) no recibe parámetros ni retorna, y `get_resultado()`
  entrega la lista ordenada. `mergesort` usa funciones privadas auxiliares
  (`_mergesort_recursivo`, `_mezclar`) que sí reciben parámetros porque son
  la implementación recursiva interna, no el método público que llama el
  main.
- **`utilidades.py`**: no tiene clases (son funciones sueltas), así que no
  rompe la regla de "una sola clase por archivo". Aquí están las funciones
  para pedir números/matrices/vectores por consola, generar listas
  aleatorias y mostrar resultados formateados.

## Cómo ejecutarlo

Requiere Python 3 (no necesita librerías externas).

```bash
cd src
python3 main.py
```

Vas a ver un menú principal:

```
=== Laboratorio 2 - Programacion 3 ===
  1. Calculadora matricial (suma, producto, inversa, matriz x vector)
  2. Ordenamiento de listas (burbuja, insercion, seleccion, mergesort, sort)
  0. Salir
```

Cada opción abre su propio submenú y, al terminar una operación, vuelve a
mostrar el submenú (no cierra el programa) hasta que eliges volver o salir.

## Pendiente / posibles mejoras para una siguiente versión

- Validaciones adicionales de entrada (por ejemplo, evitar tamaños de matriz
  negativos o cero).
- Guardar/leer matrices desde un archivo en lugar de digitarlas siempre a
  mano.
- Comparar el tiempo de ejecución de los algoritmos de ordenamiento
  (complejidad), como lo sugiere el objetivo específico del laboratorio.
