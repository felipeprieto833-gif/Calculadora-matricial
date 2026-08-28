"""
ordenador.py

Clase Ordenador: implementa el punto 3.2 del laboratorio, es decir los
algoritmos de ordenamiento (burbuja, insercion, seleccion, mergesort) y
tambien el ordenamiento con el metodo sort() nativo de Python, todos
aplicados sobre una lista de numeros flotantes.

Mismo diseno que en calculadora_matriz.py:
  - Constructor inicializa los datos miembro.
  - set_datos(lista) carga la lista a ordenar (si recibe parametro, pero
    no es un "metodo de operacion").
  - Los metodos de ordenamiento no reciben parametros ni retornan nada;
    trabajan sobre una copia de self.datos y guardan el resultado en
    self.resultado.
  - get_resultado() entrega el resultado al main.

Nota sobre mergesort: al ser un algoritmo recursivo, internamente usa
funciones auxiliares (_mezclar, _mergesort_recursivo) que si reciben
parametros (los indices del segmento a ordenar); esto es una
implementacion interna de apoyo, no el metodo publico que llama el main
(que sigue siendo mergesort(), sin parametros).
"""


class Ordenador:

    def __init__(self, datos=None):
        """Constructor: inicializa los datos miembro de la clase."""
        self.datos = datos
        self.resultado = None

    # ------------------------------------------------------------------
    def set_datos(self, datos):
        self.datos = datos

    # ------------------------------------------------------------------
    # Metodos de ordenamiento: sin parametros, sin retorno.
    # ------------------------------------------------------------------
    def burbuja(self):
        lista = list(self.datos)
        n = len(lista)
        for j in range(n - 1):
            for i in range(n - j - 1):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
        self.resultado = lista

    def insercion(self):
        lista = list(self.datos)
        for j in range(1, len(lista)):
            clave = lista[j]
            i = j - 1
            while i >= 0 and lista[i] > clave:
                lista[i + 1] = lista[i]
                i -= 1
            lista[i + 1] = clave
        self.resultado = lista

    def seleccion(self):
        lista = list(self.datos)
        n = len(lista)
        for i in range(n - 1):
            indice_minimo = i
            for j in range(i + 1, n):
                if lista[j] < lista[indice_minimo]:
                    indice_minimo = j
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        self.resultado = lista

    def mergesort(self):
        self.resultado = self._mergesort_recursivo(list(self.datos))

    def sort_python(self):
        lista = list(self.datos)
        lista.sort()
        self.resultado = lista

    # ------------------------------------------------------------------
    # Funciones auxiliares privadas para mergesort (uso interno).
    # ------------------------------------------------------------------
    def _mergesort_recursivo(self, lista):
        if len(lista) <= 1:
            return lista

        medio = len(lista) // 2
        izquierda = self._mergesort_recursivo(lista[:medio])
        derecha = self._mergesort_recursivo(lista[medio:])
        return self._mezclar(izquierda, derecha)

    def _mezclar(self, izquierda, derecha):
        resultado = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    # ------------------------------------------------------------------
    # Metodo get: entrega el resultado calculado al main.
    # ------------------------------------------------------------------
    def get_resultado(self):
        return self.resultado
