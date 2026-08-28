class Ordenador:

    def __init__(self, datos=None):
        self.datos = datos
        self.resultado = None

    def set_datos(self, datos):
        self.datos = datos

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
        self.resultado = list(self.datos)
        self._mergesort(0, len(self.resultado) - 1)

    def sort_python(self):
        lista = list(self.datos)
        lista.sort()
        self.resultado = lista

    def _mergesort(self, l, r):
        if r > l:
            m = l + (r - l) // 2
            self._mergesort(l, m)
            self._mergesort(m + 1, r)
            self._merge(l, m, r)

    def _merge(self, l, m, r):
        temp = [0] * (r - l + 1)

        i = l
        j = m + 1
        k = 0

        while i <= m and j <= r:
            if self.resultado[i] <= self.resultado[j]:
                temp[k] = self.resultado[i]
                k += 1
                i += 1
            else:
                temp[k] = self.resultado[j]
                k += 1
                j += 1

        while i <= m:
            temp[k] = self.resultado[i]
            k += 1
            i += 1

        while j <= r:
            temp[k] = self.resultado[j]
            k += 1
            j += 1

        for indice in range(l, r + 1):
            self.resultado[indice] = temp[indice - l]

    def get_resultado(self):
        return self.resultado
