"""
calculadora_matriz.py

Clase CalculadoraMatriz: implementa las operaciones matematicas del
punto 3.1 del laboratorio (suma, producto, inversa y producto matriz-vector)
usando UNICAMENTE listas de Python (no se usa numpy).

Reglas de diseno pedidas en la guia:
  - La clase tiene un metodo constructor (__init__) que inicializa los
    datos miembro.
  - Los METODOS DE OPERACION (sumar, multiplicar, invertir,
    multiplicar_por_vector) no reciben parametros ni retornan nada: leen
    el estado interno del objeto (self.matriz_a, self.matriz_b,
    self.vector) y guardan el resultado en self.resultado.
  - Para entregar el resultado al main se usa un metodo get
    (get_resultado()), tal como pide el enunciado.
  - Los "set_..." SI reciben un parametro: son la forma de cargar los
    datos de entrada en el objeto antes de pedirle que opere (equivalen
    a reconfigurar el estado interno, no son los "metodos de operacion"
    que el enunciado restringe).
"""


class CalculadoraMatriz:

    def __init__(self, matriz_a=None, matriz_b=None, vector=None):
        """Constructor: inicializa los datos miembro de la clase."""
        self.matriz_a = matriz_a
        self.matriz_b = matriz_b
        self.vector = vector
        self.resultado = None
        self.error = None

    # ------------------------------------------------------------------
    # Metodos "set": cargan los datos de entrada en el objeto.
    # ------------------------------------------------------------------
    def set_matriz_a(self, matriz):
        self.matriz_a = matriz

    def set_matriz_b(self, matriz):
        self.matriz_b = matriz

    def set_vector(self, vector):
        self.vector = vector

    def inicializar_matriz_en_ceros(self, filas, columnas):
        return [[0] * columnas for _ in range(filas)]

    # ------------------------------------------------------------------
    # Metodos de operacion: sin parametros, sin retorno.
    # ------------------------------------------------------------------
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
        """Producto matriz_a x matriz_b (columnas de A = filas de B)."""
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
        """Producto de matriz_a por vector (numero de columnas = tamano del vector)."""
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
        """
        Inversa de matriz_a por el metodo de determinante y matriz adjunta:

            A^-1 = (1 / det(A)) * adj(A)

        donde adj(A) es la TRANSPUESTA de la matriz de cofactores de A.
        Funciona para matrices cuadradas de cualquier tamano. No usa numpy:
        solo listas y aritmetica basica (el determinante se calcula de
        forma recursiva, expandiendo por la primera fila).
        """
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

    # ------------------------------------------------------------------
    # Funciones auxiliares privadas para la inversa (determinante,
    # menores, cofactores y transpuesta). Se usan solo internamente desde
    # invertir(); por eso si reciben parametros: son la implementacion de
    # apoyo, no el metodo publico de operacion que llama el main.
    # ------------------------------------------------------------------
    def _menor(self, matriz, fila_excluida, columna_excluida):
        """Submatriz que resulta de quitar una fila y una columna."""
        return [
            [valor for j, valor in enumerate(fila) if j != columna_excluida]
            for i, fila in enumerate(matriz)
            if i != fila_excluida
        ]

    def _determinante(self, matriz):
        """Determinante calculado de forma recursiva (expansion por cofactores)."""
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
        """Matriz de cofactores: cofactor[i][j] = (-1)^(i+j) * det(menor_ij)."""
        n = len(matriz)
        cofactores = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                signo = 1 if (i + j) % 2 == 0 else -1
                menor = self._menor(matriz, i, j)
                cofactores[i][j] = signo * self._determinante(menor)
        return cofactores

    def _transponer(self, matriz):
        """Transpuesta de una matriz cuadrada (o rectangular en general)."""
        filas = len(matriz)
        columnas = len(matriz[0])
        return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]

    # ------------------------------------------------------------------
    # Metodo get: entrega el resultado calculado al main.
    # ------------------------------------------------------------------
    def get_resultado(self):
        return self.resultado

    def get_error(self):
        return self.error
