import random


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Por favor ingresa un numero entero valido.")


def leer_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  Por favor ingresa un numero valido.")


def leer_matriz(nombre, filas=None, columnas=None):
    if filas is None:
        filas = leer_entero(f"Numero de filas de la matriz {nombre}: ")
    if columnas is None:
        columnas = leer_entero(f"Numero de columnas de la matriz {nombre}: ")

    matriz = []
    print(f"Ingresa los valores de la matriz {nombre} ({filas}x{columnas}):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = leer_flotante(f"  {nombre}[{i}][{j}] = ")
            fila.append(valor)
        matriz.append(fila)
    return matriz


def leer_vector(nombre, tamano=None):
    if tamano is None:
        tamano = leer_entero(f"Tamano del vector {nombre}: ")

    vector = []
    print(f"Ingresa los valores del vector {nombre} ({tamano} elementos):")
    for i in range(tamano):
        valor = leer_flotante(f"  {nombre}[{i}] = ")
        vector.append(valor)
    return vector


def generar_lista_aleatoria(cantidad, minimo=0.0, maximo=100.0):
    return [round(random.uniform(minimo, maximo), 2) for _ in range(cantidad)]


def mostrar_matriz(matriz):
    if matriz is None:
        print("(sin resultado)")
        return
    for fila in matriz:
        print("  " + "  ".join(f"{valor:8.2f}" for valor in fila))


def mostrar_vector(vector):
    if vector is None:
        print("(sin resultado)")
        return
    print("  " + "  ".join(f"{valor:8.2f}" for valor in vector))


def mostrar_lista(lista):
    if lista is None:
        print("(sin resultado)")
        return
    print("  " + ", ".join(f"{valor:.2f}" for valor in lista))


def pausar():
    input("\nPresiona ENTER para continuar...")
