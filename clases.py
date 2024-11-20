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
        
        # NO BORRAR
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

        print(f"Diagonales: {diagonales}" )
        return diagonales
      

    
matriz = [
    "A G A T C A", 
    "G A T T C A", 
    "C A A C A T", 
    "G A G C T A", 
    "A T T G C G", 
    "C T G T T C"
    ]


# #_---------------------------------------------------------------------------------------------------------------
# # #clase mutador
# # class Mutador:
# #     base_nitrogenada = ''
# #      atributos+= ''

# #     def __init__(self, base_nitrogenada):
# #         this.base_nitrogenada = base_nitrogenada
    
# #     def crear_mutante(self, mutante):
# #         return

# #clase radiacion
# class Radiacion(Mutador):
#     #mutantes horizontales y verticales
#     atributobasenitrogenada = ''
#     atributos2 = ''
#     def __init__(self): 
#         return
    
#     def crear_mutante(base_nitrogenada, posicion_inicial, orientacion_mutacion):
#         # manejo de errores
    
# #clase virus
# class Virus(Mutador):
#     #solo mutantes diagonales
#     atributobasenitrogenada = ''
#     atributos2 = ''
#     def __init__(self): 
#         return
    
#     def crear_mutante(base_nitrogenada, posicion_inicial, orientacion_mutacion):
#         # manejo de errores

# #clase sanador
# class Sanador:
#     atributos2 = ''
#     def __init__(self): 
#         return
    
#     def sanar_mutantes():
#         return



