from calculadora_matriz import CalculadoraMatriz
from ordenador import Ordenador
from utilidades import (
    leer_entero,
    leer_matriz,
    leer_vector,
    generar_lista_aleatoria,
    mostrar_matriz,
    mostrar_vector,
    mostrar_lista,
    pausar,
)


def menu_calculadora_matricial():
    calculadora = CalculadoraMatriz()

    opciones = {
        "1": "Suma de matrices",
        "2": "Producto de matrices",
        "3": "Inversa de una matriz",
        "4": "Producto de una matriz por un vector",
        "0": "Volver al menu principal",
    }

    while True:
        print("\n--- Calculadora matricial (3.1) ---")
        for clave, texto in opciones.items():
            print(f"  {clave}. {texto}")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            matriz_a = leer_matriz("A")
            matriz_b = leer_matriz("B", filas=len(matriz_a), columnas=len(matriz_a[0]))
            calculadora.set_matriz_a(matriz_a)
            calculadora.set_matriz_b(matriz_b)
            calculadora.sumar()
            if calculadora.get_error():
                print(f"Error: {calculadora.get_error()}")
            else:
                print("Resultado A + B:")
                mostrar_matriz(calculadora.get_resultado())

        elif opcion == "2":
            matriz_a = leer_matriz("A")
            columnas_b = leer_entero("Numero de columnas de la matriz B: ")
            matriz_b = leer_matriz("B", filas=len(matriz_a[0]), columnas=columnas_b)
            calculadora.set_matriz_a(matriz_a)
            calculadora.set_matriz_b(matriz_b)
            calculadora.multiplicar()
            if calculadora.get_error():
                print(f"Error: {calculadora.get_error()}")
            else:
                print("Resultado A x B:")
                mostrar_matriz(calculadora.get_resultado())

        elif opcion == "3":
            n = leer_entero("Tamano de la matriz cuadrada (n): ")
            matriz_a = leer_matriz("A", filas=n, columnas=n)
            calculadora.set_matriz_a(matriz_a)
            calculadora.invertir()
            if calculadora.get_error():
                print(f"Error: {calculadora.get_error()}")
            else:
                print("Inversa de A:")
                mostrar_matriz(calculadora.get_resultado())

        elif opcion == "4":
            matriz_a = leer_matriz("A")
            vector = leer_vector("v", tamano=len(matriz_a[0]))
            calculadora.set_matriz_a(matriz_a)
            calculadora.set_vector(vector)
            calculadora.multiplicar_por_vector()
            if calculadora.get_error():
                print(f"Error: {calculadora.get_error()}")
            else:
                print("Resultado A x v:")
                mostrar_vector(calculadora.get_resultado())

        elif opcion == "0":
            break

        else:
            print("Opcion invalida, intenta de nuevo.")
            continue

        pausar()


def menu_ordenamiento():
    ordenador = Ordenador()

    opciones = {
        "1": "Burbuja",
        "2": "Insercion",
        "3": "Seleccion",
        "4": "Mergesort",
        "5": "Sort (metodo nativo de Python)",
        "6": "Ejecutar TODOS los metodos con la misma lista",
        "0": "Volver al menu principal",
    }

    while True:
        print("\n--- Ordenamiento de listas (3.2) ---")
        for clave, texto in opciones.items():
            print(f"  {clave}. {texto}")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "0":
            break

        if opcion not in opciones:
            print("Opcion invalida, intenta de nuevo.")
            continue

        cantidad = leer_entero("Cuantos numeros aleatorios quieres generar? ")
        datos = generar_lista_aleatoria(cantidad)
        ordenador.set_datos(datos)

        print("\nLista original:")
        mostrar_lista(datos)

        if opcion == "1":
            ordenador.burbuja()
            print("Ordenada (burbuja):")
            mostrar_lista(ordenador.get_resultado())

        elif opcion == "2":
            ordenador.insercion()
            print("Ordenada (insercion):")
            mostrar_lista(ordenador.get_resultado())

        elif opcion == "3":
            ordenador.seleccion()
            print("Ordenada (seleccion):")
            mostrar_lista(ordenador.get_resultado())

        elif opcion == "4":
            ordenador.mergesort()
            print("Ordenada (mergesort):")
            mostrar_lista(ordenador.get_resultado())

        elif opcion == "5":
            ordenador.sort_python()
            print("Ordenada (sort de Python):")
            mostrar_lista(ordenador.get_resultado())

        elif opcion == "6":
            ordenador.burbuja()
            print("Burbuja:    ", end="")
            mostrar_lista(ordenador.get_resultado())

            ordenador.insercion()
            print("Insercion:  ", end="")
            mostrar_lista(ordenador.get_resultado())

            ordenador.seleccion()
            print("Seleccion:  ", end="")
            mostrar_lista(ordenador.get_resultado())

            ordenador.mergesort()
            print("Mergesort:  ", end="")
            mostrar_lista(ordenador.get_resultado())

            ordenador.sort_python()
            print("Sort Python:", end=" ")
            mostrar_lista(ordenador.get_resultado())

        pausar()


def main():
    opciones = {
        "1": "Calculadora matricial (suma, producto, inversa, matriz x vector)",
        "2": "Ordenamiento de listas (burbuja, insercion, seleccion, mergesort, sort)",
        "0": "Salir",
    }

    while True:
        print("\n=== Laboratorio 2 - Programacion 3 ===")
        for clave, texto in opciones.items():
            print(f"  {clave}. {texto}")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            menu_calculadora_matricial()
        elif opcion == "2":
            menu_ordenamiento()
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()
