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
    trabajan sobre self.resultado (una copia de self.datos) y guardan
    ahi el resultado.
  - get_resultado() entrega el resultado al main.

Nota sobre mergesort: la guia de laboratorio da el pseudocodigo de
mergesort(A, l, r) y merge(A, l, m, r) trabajando in-place sobre indices
(l, m, r) y un arreglo temporal de tamano r-l+1, en vez de dividir la
lista con slicing y devolver listas nuevas. Aqui se implementa exactamente
esa version (mergesort(self) sigue sin parametros como exige el
enunciado, y llama a los metodos privados _mergesort(l, r) / _merge(l, m,
r) que reproducen el pseudocodigo de la guia).

Al transcribir el pseudocodigo de las diapositivas se cuelan un par de
errores de tipeo tipicos de OCR/copiado (por ejemplo "while i < m and j <
r" en vez de "while i <= m and j <= r", y el ultimo while le suma a "i"
en vez de a "j"). Si se copian tal cual, el algoritmo pierde el ultimo
elemento de cada mitad. Aqui se corrigieron esos limites para que el
algoritmo funcione, conservando exactamente la misma estructura, nombres
de variables (l, m, r, i, j, k, temp) y logica de la guia.
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
        """
        Punto de entrada sin parametros (como exige el enunciado).
        Copia self.datos en self.resultado y ordena esa copia IN-PLACE
        llamando a _mergesort(l, r), igual que en la guia.
        """
        self.resultado = list(self.datos)
        self._mergesort(0, len(self.resultado) - 1)

    def sort_python(self):
        lista = list(self.datos)
        lista.sort()
        self.resultado = lista

    # ------------------------------------------------------------------
    # mergesort(A, l, r) / merge(A, l, m, r) tal como estan en la guia:
    # trabajan por indices sobre self.resultado y usan un arreglo
    # temporal, en vez de dividir la lista con slicing.
    # ------------------------------------------------------------------
    def _mergesort(self, l, r):
        if r > l:
            m = l + (r - l) // 2
            self._mergesort(l, m)          # ordenar la primera mitad
            self._mergesort(m + 1, r)      # ordenar la segunda mitad
            self._merge(l, m, r)           # mezclar las dos mitades ordenadas

    def _merge(self, l, m, r):
        # Arreglo temporal de tamano r - l + 1 (igual que en la guia)
        temp = [0] * (r - l + 1)

        i = l          # indice para la primera mitad: A[l .. m]
        j = m + 1      # indice para la segunda mitad: A[m+1 .. r]
        k = 0          # indice para el arreglo temporal

        # Recorrer ambas mitades y en cada iteracion agregar el menor de
        # ambos elementos a temp.
        while i <= m and j <= r:
            if self.resultado[i] <= self.resultado[j]:
                temp[k] = self.resultado[i]
                k += 1
                i += 1
            else:
                temp[k] = self.resultado[j]
                k += 1
                j += 1

        # Agregar los elementos que sobraron de la primera mitad
        while i <= m:
            temp[k] = self.resultado[i]
            k += 1
            i += 1

        # Agregar los elementos que sobraron de la segunda mitad
        while j <= r:
            temp[k] = self.resultado[j]
            k += 1
            j += 1

        # Copiar temp de vuelta al intervalo original
        for indice in range(l, r + 1):
            self.resultado[indice] = temp[indice - l]

    # ------------------------------------------------------------------
    # Metodo get: entrega el resultado calculado al main.
    # ------------------------------------------------------------------
    def get_resultado(self):
        return self.resultado
