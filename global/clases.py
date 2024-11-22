import random
from typing import List, Tuple, Optional

class Detector:
    """
    Clase para detectar mutaciones en una matriz de ADN. Detecta secuencias horizontales, verticales y diagonales.
    """

    def __init__(self, matriz: List[str], longitud: int = 4) -> None:
        """
        Inicializa un detector con una matriz de ADN y una longitud mínima para detectar secuencias mutantes.

        :param matriz: Lista de cadenas representando la matriz de ADN.
        :param longitud: Longitud mínima de bases consecutivas para considerar una mutación.
        """
        self.matriz = matriz
        self.longitud = longitud

    def detectar_mutantes(self, matriz: List[str]) -> bool:
        """
        Verifica si la matriz contiene mutaciones en alguna dirección (horizontal, vertical o diagonal).

        :param matriz: Matriz de ADN a analizar.
        :return: True si se detecta una mutación, False en caso contrario.
        """
        self.matriz = matriz
        return self._detectar_horizontal() or self._detectar_vertical() or self._detectar_diagonal()

    def _detectar_horizontal(self) -> bool:
        """
        Detecta secuencias mutantes en las filas de la matriz.
        :return: True si se detecta una mutación horizontal, False en caso contrario.
        """
        for fila in self.matriz:
            if self._contiene_secuencia(fila):
                return True
        return False

    def _detectar_vertical(self) -> bool:
        """
        Detecta secuencias mutantes en las columnas de la matriz.
        
        :return: True si se detecta una mutación vertical, False en caso contrario.
        """
        for col in range(len(self.matriz[0])):                             
            columna = ''.join([fila[col] for fila in self.matriz])    
            if self._contiene_secuencia(columna):
                return True
        return False

    def _detectar_diagonal(self) -> bool:
        """
        Detecta secuencias mutantes en las diagonales de la matriz.

        :return: True si se detecta una mutación diagonal, False en caso contrario.
        """
        diagonales = self._obtener_diagonales()
        for diagonal in diagonales:
            if self._contiene_secuencia(diagonal):
                return True
        return False

    def _contiene_secuencia(self, secuencia: str) -> bool:
        """
        Verifica si una secuencia contiene bases consecutivas que formen una mutación.

        :param secuencia: Cadena que representa una secuencia de ADN.
        :return: True si contiene una mutación, False en caso contrario.
        """
        for base in "ATCG":
            if base * self.longitud in secuencia:
                return True
        return False
        
    def _obtener_diagonales(self) -> list[str]:
        """
        Obtiene todas las diagonales de la matriz, tanto descendentes como ascendentes.

        :return: Lista de cadenas representando las diagonales de la matriz.
        """
        diagonales = []
        n = len(self.matriz)

        for i in range(n - 3):  
            diagonal1 = ''
            diagonal2 = ''
            for j in range(n - i):
                if i + j < n:
                    diagonal1 += self.matriz[i + j][j]     
                    diagonal2 += self.matriz[j][i + j]     
            if len(diagonal1) >= 4:
                diagonales.append(diagonal1)
            if len(diagonal2) >= 4:
                diagonales.append(diagonal2)

        for i in range(3, n):
            diagonal1 = ''
            diagonal2 = ''
            for j in range(i + 1):
                diagonal1 += self.matriz[i - j][j]         
                diagonal2 += self.matriz[n - j - 1][i - j] 
            if len(diagonal1) >= 4:
                diagonales.append(diagonal1)
            if len(diagonal2) >= 4:
                diagonales.append(diagonal2)

        return diagonales

class Mutador:
    """
    Clase base para la creación de mutantes en la matriz de ADN.
    """
    def __init__(self, base_nitrogenada: str, nombre: str, matriz: List[str]) -> None:
        """
        Inicializa un mutador con su base nitrogenada, nombre y matriz de ADN.

        :param base_nitrogenada: Base nitrogenada utilizada para la mutación.
        :param nombre: Nombre del mutador.
        :param matriz: Matriz de ADN original.
        """
        self.base_nitrogenada = base_nitrogenada  
        self.nombre = nombre                      
        self.matriz = matriz                   

    def crear_mutante(self) -> None:
        """
        Método abstracto para implementar en las clases derivadas.
        """
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")

class Radiacion(Mutador):
    """
        Clase radiacion que es hija de mutador.
    """ 
    def __init__(self, base_nitrogenada: str, nombre: str, matriz: list) -> None: 
        super().__init__(base_nitrogenada, nombre, matriz)
        self.orientacion_mutacion = None

    def crear_mutante(self, base_nitrogenada: str, posicion_inicial: Tuple[int,int], orientacion_mutacion: str) -> Optional[list[str]]:
        """
        Crea un mutante aplicando radiación en una dirección específica.

        :param base_nitrogenada: Base nitrogenada utilizada para la mutación.
        :param posicion_inicial: Posición inicial de la mutación (x, y).
        :param orientacion_mutacion: Dirección de la mutación ('H' para horizontal, 'V' para vertical).
        :return: Nueva matriz con la mutación aplicada, o None si hubo un error.
        """
        try:
            x, y = posicion_inicial
            n = len(self.matriz)

            matriz_mutable = [list(fila) for fila in self.matriz]

            if orientacion_mutacion == "H":
                if y + 3 >= n:
                    raise ValueError("La mutación horizontal excede los límites de la matriz.")
                for i in range(4):
                    matriz_mutable[x][y + i] = base_nitrogenada  

            elif orientacion_mutacion == "V":
                if x + 3 >= n:
                    raise ValueError("La mutación vertical excede los límites de la matriz.")
                for i in range(4):
                    matriz_mutable[x + i][y] = base_nitrogenada  

            else:
                raise ValueError("La orientación debe ser 'H' o 'V'.")

            self.matriz = [''.join(fila) for fila in matriz_mutable]
            print(f"Mutación creada exitosamente con {self.nombre}.")
            return self.matriz

        except ValueError as e:
            print(f"Error: {e}")
            return self.matriz

class Virus(Mutador):
    """
    Clase que aplica mutaciones diagonales a una matriz de ADN mediante un virus.
    """
    def __init__(self, nombre: str, base_nitrogenada: str, matriz: List[str]) -> None:
        """
        Inicializa un virus con su base nitrogenada, nombre y la matriz de ADN original.

        :param nombre: Nombre del virus.
        :param base_nitrogenada: Base nitrogenada utilizada para la mutación.
        :param matriz: Matriz de ADN donde se aplicará la mutación.
        """
        super().__init__(base_nitrogenada, nombre, matriz)
        self.matriz = None

    def crear_mutante(self, matriz: List[str], base_nitrogenada: str, posicion_inicial: Tuple[int, int]) -> Optional[List[str]]:
        """
        Crea un mutante aplicando una mutación diagonal en la matriz de ADN.

        :param matriz: Matriz de ADN a modificar.
        :param base_nitrogenada: Base nitrogenada utilizada para la mutación.
        :param posicion_inicial: Posición inicial (x, y) para comenzar la mutación diagonal.
        :return: Nueva matriz con la mutación aplicada, o None si hubo un error.
        """
        try:
            self.matriz = [list(fila) for fila in matriz]  

            if not self._validar_posicion(posicion_inicial):
                print(f"Posición inicial inválida: {posicion_inicial}")
                return matriz

            x, y = posicion_inicial
            for i in range(4):
                self.matriz[x + i][y + i] = base_nitrogenada
            self.matriz = [''.join(fila) for fila in self.matriz] 
            return self.matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return matriz

    def _validar_posicion(self, posicion_inicial: tuple):
        x, y = posicion_inicial
        n = len(self.matriz)
        if x < 0 or y < 0 or x + 3 >= n or y + 3 >= n:
            return False
        return True

import random
  
class Sanador:
    """
    Clase que se encarga de sanar las mutaciones en una matriz de ADN generando una nueva sin mutaciones.
    """
    def __init__(self, nombre: str, detector: Detector) -> None:
        """
        Inicializa un sanador con su nombre y un detector para identificar mutaciones en la matriz de ADN.

        :param nombre: Nombre del sanador.
        :param detector: Objeto Detector que se utiliza para identificar mutaciones en la matriz de ADN.
        """
        self.nombre = nombre
        self.detector = detector

    def sanar_mutantes(self, matriz: List[str]) -> List[str]:
        """
        Detecta mutantes en la matriz de ADN y genera una nueva matriz sin mutantes si se encuentran.

        :param matriz: Matriz de ADN a analizar.
        :return: Nueva matriz de ADN sana si se detectan mutantes, o la matriz original si no se detectan.
        """
        if self.detector.detectar_mutantes(matriz):
            print("Mutaciones detectadas. Generando nuevo ADN...")
            return self._generar_adn_sano(len(matriz))
        else:
            print("No se detectaron mutaciones.")
            return matriz

    def _generar_adn_sano(self, tamanio: int) -> List[str]:
        """
        Genera una nueva matriz de ADN aleatoria que no contenga mutantes.

        :param tamanio: El tamaño de la matriz de ADN que se generará.
        :return: Matriz de ADN sana generada aleatoriamente.
        """
        bases = ["A", "T", "C", "G"]
        while True:  
            nuevo_adn = []
            for _ in range(tamanio):
                fila = ''.join(random.choice(bases) for _ in range(tamanio))
                nuevo_adn.append(fila)
            if not self.detector.detectar_mutantes(nuevo_adn):  
                print("Nueva matriz de ADN generada sin mutantes.")
                return nuevo_adn
            else:
                print("Se generó ADN con mutantes. Regenerando...")
