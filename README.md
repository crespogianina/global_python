                                     | GLOBAL PYTHON | 1 PROGRAMACION 2 | 2024 |
                            Proyecto de Detección, Sanación y Creación de Mutaciones en ADN

DESCRIPCION:
Este proyecto permite detectar, generar y sanar mutaciones en una secuencia de ADN representada en una matriz de 6x6. Las mutaciones pueden ser horizontales, verticales o diagonales, y se consideran mutantes cuando una base nitrogenada se repite al menos 4 veces consecutivas.

PARTICIPANTES:
|Gianina Crespo
|Johana Quiroga
|Constanza Trubiano

---

                                               |REQUISITOS|

-Python 3.x
-No se requieren paquetes adicionales (se utilizan tipos nativos de datos en Python).

---

                                               |INSTALACION|

-Clona este repositorio en tu maquina local (git clone)
-Navega al directorio del proyecto (cd tu_repositorio)

---

                                                  | USO |
                                          |EJECUCION DEL PROGRAMA|

-Para ejecutar el programa, simplemente corre el archivo ejecutable.py (python ejecutable.py)

                                              |MENU PRINCIPAL|

Al ejecutar el programa, se te presentará un menú con las siguientes opciones:

1. Detectar mutaciones: Detecta si hay mutaciones en la matriz de ADN actual.
2. Generar mutaciones: Genera mutaciones en la matriz de ADN actual.
3. Sanar ADN: Sana cualquier mutación en la matriz de ADN actual.
4. Ingresar una nueva matriz: Permite ingresar una nueva matriz de ADN.
5. Salir del menú: Sale del programa.

---

                                          |INSTRUCCIONES DETALLADAS|

1. Detectar Mutaciones
   Selecciona la opción 1 para detectar mutaciones en la matriz de ADN actual. El programa te informará si se encontraron mutaciones y mostrará la matriz de ADN.

2. Generar Mutaciones
   Selecciona la opción 2 para generar mutaciones. Se te preguntará si deseas generar un virus o una radiación:
   -Virus: Crea mutaciones diagonales.
   -Radiación: Crea mutaciones horizontales o verticales.
   Sigue las instrucciones para ingresar el nombre, la posición inicial y la base nitrogenada para la mutación.

3. Sanar ADN
   Selecciona la opción 3 para sanar cualquier mutación en la matriz de ADN actual. El programa generará aleatoriamente un ADN completamente nuevo si se detectan mutaciones.

4. Ingresar una Nueva Matriz
   Selecciona la opción 4 para ingresar una nueva matriz de ADN. Se te pedirá que ingreses las 6 filas de la matriz, asegurándote de que cada fila tenga 6 bases nitrogenadas (A, T, C, G).

5. Salir del Menú
   Selecciona la opción 5 para salir del programa.

---

                                                |EJEMPLO DE USO|

Ingrese un ADN
Fila 1: AGATCA
Fila 2: GATTCA
Fila 3: CAACAT
Fila 4: GAGCTA
Fila 5: ATTGCG
Fila 6: CTGTTC
La matriz es la siguiente:
A G A T C A
G A T T C A
C A A C A T
G A G C T A
A T T G C G
C T G T T C
------------------MENÚ-------------------
|1. Detectar mutaciones
|2. Generar mutaciones
|3. Sanar ADN
|4. Ingresar una nueva matriz
|5. Salir del menu

---

Ingrese una opcion: 1
Vamos a detectar mutaciones...
No se encontraron mutaciones en el ADN.

---
