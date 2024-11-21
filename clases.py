#clase detector uwu
class Detector:
    def __init__(self):
        self.matriz = []
        self.longitud = 4  

    def detectar_mutantes(self, matriz):
        self.matriz = matriz
        return self._detectar_horizontal() or self._detectar_vertical() or self._detectar_diagonal()

    def _detectar_horizontal(self):
        for fila in self.matriz:
            if self._contiene_secuencia(fila):
                return True
        return False

    def _detectar_vertical(self):
        for col in range(len(self.matriz[0])):      
            #para chekiar                                 
            columna = ''.join([fila[col] for fila in self.matriz])    
            if self._contiene_secuencia(columna):
                return True
        return False

    def _detectar_diagonal(self):
        diagonales = self._obtener_diagonales()
        for diagonal in diagonales:
            if self._contiene_secuencia(diagonal):
                return True
        return False

    def _contiene_secuencia(self, secuencia):
        for base in "ATCG":
            if base * self.longitud in secuencia: # A * 4 => AAAA
                return True
        return False
        
    def _obtener_diagonales(self):
        diagonales = []
        n = len(self.matriz)

        # Diagonales descendentes desde la columna izquierda
        for i in range(n):
            diagonal = ''
            for k in range(n - i):
                if i + k < n:
                    diagonal += self.matriz[i + k][k]
                    if len(diagonal) > 3:
                        diagonales.append(diagonal)
                        
        # Diagonales descendentes desde la fila superior derecha (excluyendo la primera fila)
        for i in range(1, n):
            diagonal = ''
            for k in range(n - i):
                diagonal += self.matriz[k][n - k - i]
                if len(diagonal) > 3:
                    diagonales.append(diagonal)
                
        # Diagonales descendentes desde la columna derecha
        for i in range(n):
            diagonal = ''
            for k in range(n - i):
                if i + k < n:
                    diagonal += self.matriz[i + k][n - 1 - k]
                    if len(diagonal) > 3:
                        if diagonal in diagonales:
                            pass
                        else: 
                            diagonales.append(diagonal)


        # Diagonales descendentes desde la fila superior derecha (excluye la principal)
        for j in range(1, n):
            diagonal = ''
            for k in range(n - j):
                diagonal += self.matriz[k][n - 1 - (j + k)]
                if len(diagonal) > 3:
                    if diagonal in diagonales:
                        pass
                    else: 
                        diagonales.append(diagonal)
        return diagonales

#fin clase detector 
# #---------------------------------------------------------------------------------------------------------------
# # #clase mutador
class Mutador:

    def __init__(self, base_nitrogenada, nombre):
        self.base_nitrogenada = base_nitrogenada
        self.nombre = nombre 
        self.matriz = None
        # self.clase = clase 
    
    def crear_mutante(self, mutante):
        pass

# #clase radiacion
class Radiacion(Mutador):

    def __init__(self, base_nitrogenada): 
        super().__init__(base_nitrogenada, nombre='Radiacion')
        self.orientacion_mutacion = None
    
    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_mutacion):
        #mutantes horizontales y verticales
        try:
            x,y = posicion_inicial
            if orientacion_mutacion == "H":
                for i in range(4):
                    matriz[x][y + i] =  base_nitrogenada
            elif orientacion_mutacion == "V":
                for i in range(4):
                    matriz[x + i][y] = base_nitrogenada
            return matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}") 
            return None

    
# #clase virus hija de mutador
class Virus(Mutador):
    def __init__(self, nombre, base_nitrogenada):
        super().__init__(base_nitrogenada, nombre)
        self.matriz = None

    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial):
        try:
            self.matriz = [list(fila) for fila in matriz]  

            if not self._validar_posicion(posicion_inicial):
                print(f"Posición inicial inválida: {posicion_inicial}")
                return None

            x, y = posicion_inicial
            for i in range(4):
                self.matriz[x + i][y + i] = base_nitrogenada
            self.matriz = [''.join(fila) for fila in self.matriz]  
            return self.matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return None

    def _validar_posicion(self, posicion_inicial):
        x, y = posicion_inicial
        n = len(self.matriz)
        if x < 0 or y < 0 or x + 3 >= n or y + 3 >= n:
            return False
        return True


 #clase sanador
import random

class Sanador:
    def __init__(self, detector):
        self.detector = detector
        self.nueva_matriz = None

    def sanar_mutantes(self, matriz):
        # Verificar si hay mutaciones en la matriz
        if self.detector.detectar_mutantes(matriz):
            print("Se detectaron mutaciones. Sanando...")
            bases = ['A', 'T', 'C', 'G']
            # Generar una nueva matriz sin mutaciones
            nueva_matriz = [''.join(random.choice(bases) for _ in range(6)) for _ in range(6)]
            while self.detector.detectar_mutantes(nueva_matriz):
                nueva_matriz = [''.join(random.choice(bases) for _ in range(6)) for _ in range(6)]
            print("Mutaciones eliminadas. Nueva matriz de ADN generada:")
            for fila in nueva_matriz:
                print(fila)
            return nueva_matriz
        else:
            print("No se detectaron mutaciones. No es necesario sanar.")
            return matriz
