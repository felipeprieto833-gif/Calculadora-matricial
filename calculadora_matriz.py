class CalculadoraMatriz:

    def __init__(self, matriz_a=None, matriz_b=None, vector=None):
        self.matriz_a = matriz_a
        self.matriz_b = matriz_b
        self.vector = vector
        self.resultado = None
        self.error = None

    def set_matriz_a(self, matriz):
        self.matriz_a = matriz

    def set_matriz_b(self, matriz):
        self.matriz_b = matriz

    def set_vector(self, vector):
        self.vector = vector

    def inicializar_matriz_en_ceros(self, filas, columnas):
        return [[0] * columnas for _ in range(filas)]

    def sumar(self):
        self.error = None
        self.resultado = None

        filas = len(self.matriz_a)
        columnas = len(self.matriz_a[0])

        if len(self.matriz_b) != filas or len(self.matriz_b[0]) != columnas:
            self.error = "Las matrices deben tener las mismas dimensiones para sumarse."
            return

        suma = self.inicializar_matriz_en_ceros(filas, columnas)
        for i in range(filas):
            for j in range(columnas):
                suma[i][j] = self.matriz_a[i][j] + self.matriz_b[i][j]

        self.resultado = suma

    def multiplicar(self):
        self.error = None
        self.resultado = None

        filas_a = len(self.matriz_a)
        columnas_a = len(self.matriz_a[0])
        filas_b = len(self.matriz_b)
        columnas_b = len(self.matriz_b[0])

        if columnas_a != filas_b:
            self.error = (
                "No se pueden multiplicar: el numero de columnas de la "
                "matriz A debe ser igual al numero de filas de la matriz B."
            )
            return

        producto = self.inicializar_matriz_en_ceros(filas_a, columnas_b)
        for i in range(filas_a):
            for j in range(columnas_b):
                suma = 0
                for k in range(columnas_a):
                    suma += self.matriz_a[i][k] * self.matriz_b[k][j]
                producto[i][j] = suma

        self.resultado = producto

    def multiplicar_por_vector(self):
        self.error = None
        self.resultado = None

        filas = len(self.matriz_a)
        columnas = len(self.matriz_a[0])

        if len(self.vector) != columnas:
            self.error = (
                "El tamano del vector debe ser igual al numero de "
                "columnas de la matriz."
            )
            return

        resultado = [0] * filas
        for i in range(filas):
            suma = 0
            for j in range(columnas):
                suma += self.matriz_a[i][j] * self.vector[j]
            resultado[i] = suma

        self.resultado = resultado

    def invertir(self):
        self.error = None
        self.resultado = None

        n = len(self.matriz_a)
        for fila in self.matriz_a:
            if len(fila) != n:
                self.error = "La inversa solo esta definida para matrices cuadradas."
                return

        determinante = self._determinante(self.matriz_a)
        if determinante == 0:
            self.error = "La matriz es singular (determinante = 0): no tiene inversa."
            return

        matriz_cofactores = self._matriz_cofactores(self.matriz_a)
        adjunta = self._transponer(matriz_cofactores)

        self.resultado = [
            [adjunta[i][j] / determinante for j in range(n)] for i in range(n)
        ]

    def _menor(self, matriz, fila_excluida, columna_excluida):
        resultado =  [
            [valor for j, valor in enumerate(fila) if j != columna_excluida]
            for i, fila in enumerate(matriz)
            if i != fila_excluida
        ]
        return resultado

    def _determinante(self, matriz):
        n = len(matriz)

        if n == 1:
            return matriz[0][0]

        if n == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

        determinante = 0
        for columna in range(n):
            signo = 1 if columna % 2 == 0 else -1
            menor = self._menor(matriz, 0, columna)
            determinante += signo * matriz[0][columna] * self._determinante(menor)
        return determinante

    def _matriz_cofactores(self, matriz):
        n = len(matriz)
        cofactores = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                signo = 1 if (i + j) % 2 == 0 else -1
                menor = self._menor(matriz, i, j)
                cofactores[i][j] = signo * self._determinante(menor)
        return cofactores

    def _transponer(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]

    def get_resultado(self):
        return self.resultado

    def get_error(self):
        return self.error
