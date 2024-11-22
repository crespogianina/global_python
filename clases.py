#clase detector uwu
#Clase vieja detector
# class Detector:
#     def __init__(self):
#         self.matriz = []
#         self.longitud = 4  

#     def detectar_mutantes(self, matriz):
#         self.matriz = matriz
#         return self._detectar_horizontal() or self._detectar_vertical() or self._detectar_diagonal()

#     def _detectar_horizontal(self):
#         for fila in self.matriz:
#             if self._contiene_secuencia(fila):
#                 return True
#         return False

#     def _detectar_vertical(self):
#         for col in range(len(self.matriz[0])):      
#             #para chekiar                                 
#             columna = ''.join([fila[col] for fila in self.matriz])    
#             if self._contiene_secuencia(columna):
#                 return True
#         return False

#     def _detectar_diagonal(self):
#         diagonales = self._obtener_diagonales()
#         for diagonal in diagonales:
#             if self._contiene_secuencia(diagonal):
#                 return True
#         return False

#     def _contiene_secuencia(self, secuencia):
#         for base in "ATCG":
#             if base * self.longitud in secuencia: # A * 4 => AAAA
#                 return True
#         return False
        
#     def _obtener_diagonales(self):
#         diagonales = []
#         n = len(self.matriz)

#         # Diagonales descendentes desde la columna izquierda
#         for i in range(n):
#             diagonal = ''
#             for k in range(n - i):
#                 if i + k < n:
#                     diagonal += self.matriz[i + k][k]
#                     if len(diagonal) > 3:
#                         diagonales.append(diagonal)
                        
#         # Diagonales descendentes desde la fila superior derecha (excluyendo la primera fila)
#         for i in range(1, n):
#             diagonal = ''
#             for k in range(n - i):
#                 diagonal += self.matriz[k][n - k - i]
#                 if len(diagonal) > 3:
#                     diagonales.append(diagonal)
                
#         # Diagonales descendentes desde la columna derecha
#         for i in range(n):
#             diagonal = ''
#             for k in range(n - i):
#                 if i + k < n:
#                     diagonal += self.matriz[i + k][n - 1 - k]
#                     if len(diagonal) > 3:
#                         if diagonal in diagonales:
#                             pass
#                         else: 
#                             diagonales.append(diagonal)


#         # Diagonales descendentes desde la fila superior derecha (excluye la principal)
#         for j in range(1, n):
#             diagonal = ''
#             for k in range(n - j):
#                 diagonal += self.matriz[k][n - 1 - (j + k)]
#                 if len(diagonal) > 3:
#                     if diagonal in diagonales:
#                         pass
#                     else: 
#                         diagonales.append(diagonal)
#         return diagonales

#Clase nueva
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
            if base * self.longitud in secuencia:
                return True
        return False
        
    def _obtener_diagonales(self):
        diagonales = []
        n = len(self.matriz)

        # Diagonales descendentes (de izquierda a derecha)
        for i in range(n - 3):  # Solo necesitamos analizar diagonales con al menos 4 elementos
            diagonal1 = ''
            diagonal2 = ''
            for j in range(n - i):
                if i + j < n:
                    diagonal1 += self.matriz[i + j][j]     # Diagonal descendente principal
                    diagonal2 += self.matriz[j][i + j]     # Diagonal descendente secundaria
            if len(diagonal1) >= 4:
                diagonales.append(diagonal1)
            if len(diagonal2) >= 4:
                diagonales.append(diagonal2)

        # Diagonales ascendentes (de derecha a izquierda)
        for i in range(3, n):
            diagonal1 = ''
            diagonal2 = ''
            for j in range(i + 1):
                diagonal1 += self.matriz[i - j][j]         # Diagonal ascendente principal
                diagonal2 += self.matriz[n - j - 1][i - j] # Diagonal ascendente secundaria
            if len(diagonal1) >= 4:
                diagonales.append(diagonal1)
            if len(diagonal2) >= 4:
                diagonales.append(diagonal2)

        return diagonales


#fin clase detector 
# #---------------------------------------------------------------------------------------------------------------
# # #clase mutador vieja
# class Mutador:

#     def __init__(self, base_nitrogenada, nombre):
#         self.base_nitrogenada = base_nitrogenada
#         self.nombre = nombre 
#         self.matriz = None
#         # self.clase = clase 
    
#     def crear_mutante(self, mutante):
#         pass

#Clase mutador nueva
class Mutador:
    def __init__(self, base_nitrogenada, nombre, matriz):
        self.base_nitrogenada = base_nitrogenada  # Atributo que indica cuál base se repetirá 4 veces
        self.nombre = nombre                      # Atributo adicional: nombre del mutador
        self.matriz = matriz                   # Atributo adicional: nivel de mutación

    def crear_mutante(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")


# # #clase radiacion vieja
# class Radiacion(Mutador):

#     def __init__(self, base_nitrogenada, nombre): 
#         super().__init__(base_nitrogenada, nombre)
#         self.orientacion_mutacion = None
    
#     def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_mutacion):
#         #mutantes horizontales y verticales
#         try:
#             x,y = posicion_inicial
#             if orientacion_mutacion == "H":
#                 for i in range(4):
#                     matriz[x][y + i] =  base_nitrogenada
#             elif orientacion_mutacion == "V":
#                 for i in range(4):
#                     matriz[x + i][y] = base_nitrogenada
#             return matriz
#         except Exception as e:
#             print(f"Error al crear mutante: {e}") 
#             return None

#Clase radiacion nueva
# class Radiacion(Mutador):
#     def __init__(self, base_nitrogenada, nombre, matriz): 
#         super().__init__(base_nitrogenada, nombre, matriz)
#         self.orientacion_mutacion = None

#     def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_mutacion):
#         # Mutantes horizontales y verticales
#         try:
#             x, y = posicion_inicial
#             if orientacion_mutacion == "H" and y + 3 < len(matriz[0]):
#                 for i in range(4):
#                     matriz[x][y + i] = base_nitrogenada
#             elif orientacion_mutacion == "V" and x + 3 < len(matriz):
#                 for i in range(4):
#                     matriz[x + i][y] = base_nitrogenada
#             else:
#                 raise ValueError("Posición o orientación no válida para mutación")
#             return matriz
#         except Exception as e:
#             print(f"Error al crear mutante: {e}") 
#             return matriz

# class Radiacion(Mutador):
#     def __init__(self, base_nitrogenada, nombre, matriz): 
#         super().__init__(base_nitrogenada, nombre, matriz)
#         self.orientacion_mutacion = None

#     def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_mutacion):
#         try:
#             # Verificar que posicion_inicial sea válida
#             if not isinstance(posicion_inicial, (list, tuple)) or len(posicion_inicial) != 2:
#                 raise ValueError("posicion_inicial debe ser una lista o tupla con dos elementos")

#             x, y = posicion_inicial  # Desempaquetar posición inicial
            
#             # Mutación horizontal
#             if orientacion_mutacion == "H" and y + 3 < len(matriz[0]):
#                 for i in range(4):
#                     matriz[x][y + i] = base_nitrogenada
#             # Mutación vertical
#             elif orientacion_mutacion == "V" and x + 3 < len(matriz):
#                 for i in range(4):
#                     matriz[x + i][y] = base_nitrogenada
#             else:
#                 raise ValueError("Posición o orientación no válida para mutación")

#             return matriz

#         except Exception as e:
#             print(f"Error al crear mutante: {e}") 
#             return matriz

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, nombre, matriz): 
        super().__init__(base_nitrogenada, nombre, matriz)
        self.orientacion_mutacion = None

    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_mutacion):
        try:
            x, y = posicion_inicial
            n = len(matriz)
            
            # Verificar límites de la matriz y orientación
            if orientacion_mutacion == "H":
                if y + 3 >= n:
                    raise ValueError("La mutación horizontal excede los límites de la matriz.")
                for i in range(4):
                    matriz[x][y + i] = base_nitrogenada
            
            elif orientacion_mutacion == "V":
                if x + 3 >= n:
                    raise ValueError("La mutación vertical excede los límites de la matriz.")
                for i in range(4):
                    matriz[x + i][y] = base_nitrogenada
            
            else:
                raise ValueError("La orientación debe ser 'H' o 'V'.")

            print(f"Mutación creada exitosamente con {self.nombre}.")
            return matriz

        except ValueError as e:
            print(f"Error: {e}")
            return None

        except Exception as e:
            print(f"Error inesperado: {e}")
            return None



# # #clase virus hija de mutador vieja
# class Virus(Mutador):
#     def __init__(self, nombre, base_nitrogenada):
#         super().__init__(base_nitrogenada, nombre)
#         self.matriz = None

#     def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial):
#         try:
#             self.matriz = [list(fila) for fila in matriz]  

#             if not self._validar_posicion(posicion_inicial):
#                 print(f"Posición inicial inválida: {posicion_inicial}")
#                 return None

#             x, y = posicion_inicial
#             for i in range(4):
#                 self.matriz[x + i][y + i] = base_nitrogenada
#             self.matriz = [''.join(fila) for fila in self.matriz]  
#             return self.matriz
#         except Exception as e:
#             print(f"Error al crear mutante: {e}")
#             return None

#     def _validar_posicion(self, posicion_inicial):
#         x, y = posicion_inicial
#         n = len(self.matriz)
#         if x < 0 or y < 0 or x + 3 >= n or y + 3 >= n:
#             return False
#         return True

# #clase virus hija de mutador nueva
class Virus(Mutador):
    def __init__(self, nombre, base_nitrogenada, matriz):
        super().__init__(base_nitrogenada, nombre, matriz)
        self.matriz = None

    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial):
        try:
            self.matriz = [list(fila) for fila in matriz]  # Convertir filas a listas para mutación

            if not self._validar_posicion(posicion_inicial):
                print(f"Posición inicial inválida: {posicion_inicial}")
                return matriz

            x, y = posicion_inicial
            for i in range(4):
                self.matriz[x + i][y + i] = base_nitrogenada
            self.matriz = [''.join(fila) for fila in self.matriz]  # Convertir filas de vuelta a strings
            return self.matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return matriz

    def _validar_posicion(self, posicion_inicial):
        x, y = posicion_inicial
        n = len(self.matriz)
        if x < 0 or y < 0 or x + 3 >= n or y + 3 >= n:
            return False
        return True


#  #clase sanador vieja
# import random

# class Sanador:
#     def __init__(self, detector):
#         self.detector = detector
#         self.nueva_matriz = None

#     def sanar_mutantes(self, matriz):
#         # Verificar si hay mutaciones en la matriz
#         if self.detector.detectar_mutantes(matriz):
#             print("Se detectaron mutaciones. Sanando...")
#             bases = ['A', 'T', 'C', 'G']
#             # Generar una nueva matriz sin mutaciones
#             nueva_matriz = [''.join(random.choice(bases) for _ in range(6)) for _ in range(6)]
#             while self.detector.detectar_mutantes(nueva_matriz):
#                 nueva_matriz = [''.join(random.choice(bases) for _ in range(6)) for _ in range(6)]
#             print("Mutaciones eliminadas. Nueva matriz de ADN generada:")
#             for fila in nueva_matriz:
#                 print(fila)
#             return nueva_matriz
#         else:
#             print("No se detectaron mutaciones. No es necesario sanar.")
#             return matriz



#clase sanador nueva

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
