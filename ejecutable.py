from clases import Detector, Virus, Radiacion, Sanador
import os
from typing import List, Tuple

# Matriz global que almacena el ADN ingresado por el usuario
matriz: List[List[str]] = []

def main() -> None:
    """
    Función principal que inicia el programa y muestra el menú pyal usuario.
    """
    menu()

def menu() -> None:
    """
    Muestra el menú principal al usuario y maneja las opciones seleccionadas.
    """
    global matriz
    print("\033[[94m" + "Ingrese un ADN inicial")
    matriz = ingresar_nueva_matriz()
    mostrar_matriz(matriz)

    while True:
        print("\033[1;36m" + "------------------MENÚ-------------------")
        print("\033[94m" + "|1. Detectar mutaciones")
        print("\033[94m" + "|2. Generar mutaciones")
        print("\033[94m" + "|3. Sanar ADN")
        print("\033[94m" + "|4. Ingresar una nueva matriz")
        print("\033[94m" + "|5. Salir del menú")
        print("\033[1;36m" + "-----------------------------------------")
        opcion = input("\033[97m" + "Ingrese una opción: ")

        limpiar_terminal()

        if opcion == "1":
            detectar_mutaciones_matriz()
        elif opcion == "2":
            matriz = generar_mutaciones(matriz)
        elif opcion == "3":
            matriz = sanar_mutaciones(matriz)
        elif opcion == "4":
            matriz = ingresar_nueva_matriz()
        elif opcion == "5":
            salir_menu()
            break
        else:
            print("\033[94m" + "Debe ingresar una opción válida.")
            print("\033[94m" + "Intente nuevamente.")

def detectar_mutaciones_matriz() -> None:
    """
    Detecta si existen mutaciones en la matriz de ADN actual.
    """
    print("\033[94m" + "Vamos a detectar mutaciones...")
    detector = Detector(matriz)
    mutaciones_detectadas = detector.detectar_mutantes(matriz)

    if mutaciones_detectadas:
        print("\033[94m" + "Se encontraron mutaciones en el ADN.")
        mostrar_matriz(matriz)
    else:
        print("\033[94m" + "No se encontraron mutaciones en el ADN.")

def generar_mutaciones(matriz) -> List[List[str]]:
    """
    Solicita al usuario el tipo de mutación (Virus o Radiación) y la genera.
    """
    print("\033[94m" + "Generando mutaciones...")
    while True:
        print("\033[94m" + "¿Desea generar un Virus o una Radiación?")
        mutacion = input("\033[97m" + "Virus o Radiación: ").lower()
        limpiar_terminal()

        if mutacion == "virus":
            return generar_virus(matriz)
            
        elif mutacion == "radiacion":
            return generar_radiacion(matriz)
            
        else:
            print("\033[94m" + "Ingrese una opción válida.")

def generar_virus(matriz) -> List[List[str]]:
    """
    Solicita al usuario los datos para generar un Virus y lo aplica en la matriz de ADN.
    """
    print("\033[94m" + "Ingrese el nombre del virus:")
    nombre = input("\033[97m" + "Nombre: ").capitalize()
    limpiar_terminal()

    if not nombre:
        print("\033[94m" + "Debe ingresar un nombre.")
        return generar_virus()

    print("\033[94m" + "Ingrese la posición inicial (fila, columna):")
    try:
        posicion_inicial = tuple(map(int, input("\033[97m" + "Posición inicial: ").split(',')))
        limpiar_terminal()
    except ValueError:
        print("\033[94m" + "Debe ingresar una posición válida.")
        return generar_virus()

    nuevo_virus = agregar_base_nitrogenada(matriz, posicion_inicial, nombre)
    if nuevo_virus:
        mostrar_matriz(nuevo_virus)
        return nuevo_virus
    else:
        print("\033[94m" + "No se pudo generar el virus.")

def agregar_base_nitrogenada(matriz: List[List[str]], posicion_inicial: Tuple[int, int], nombre: str) -> List[List[str]]:
    """
    Agrega una base nitrogenada en la matriz de ADN, generando un Virus.

    Args:
        matriz (List[List[str]]): Matriz de ADN actual.
        posicion_inicial (Tuple[int, int]): Coordenadas iniciales para la mutación.
        nombre (str): Nombre del virus.

    Returns:
        List[List[str]]: Matriz de ADN actualizada con el Virus.
    """
    print("\033[94m" + "Ingrese la base nitrogenada que desee:")
    print("\033[94m" + "| A | C | G | T |")
    base = input("\033[97m" + "Ingrese la opción: ").upper()
    limpiar_terminal()

    if base in ["A", "C", "G", "T"]:
        virus = Virus(base, nombre, matriz)
        return virus.crear_mutante(matriz, base, posicion_inicial)
    else:
        print("\033[94m" + "Ingrese una base nitrogenada válida.")
        return agregar_base_nitrogenada(matriz, posicion_inicial, nombre)

def generar_radiacion(matriz) -> List[List[str]]:
    """
    Solicita al usuario los datos para generar una Radiación y la aplica en la matriz de ADN.
    """
    nombre = input("\033[94m" + "Ingrese el nombre de la radiación: ").capitalize()
    if not nombre:
        print("\033[94m" + "Debe ingresar un nombre para la radiación.")
        return generar_radiacion()

    orientacion = input("\033[94m" + "Ingrese la orientación (H: Horizontal, V: Vertical): ").upper()
    if orientacion not in ["H", "V"]:
        print("\033[94m" + "Debe ingresar una orientación válida.")
        return generar_radiacion()

    print("\033[94m" + "Ingrese la posición inicial (fila, columna):")
    try:
        posicion_inicial = tuple(map(int, input("\033[97m" + "Posición inicial: ").split(',')))
    except ValueError:
        print("\033[94m" + "Debe ingresar una posición válida.")
        return generar_radiacion()

    base = input("\033[94m" + "Ingrese la base nitrogenada (A, C, G, T): ").upper()
    if base not in ["A", "C", "G", "T"]:
        print("\033[94m" + "Debe ingresar una base nitrogenada válida.")
        return generar_radiacion()

    radiacion = Radiacion(base, nombre, matriz)
    nueva_matriz = radiacion.crear_mutante(base, posicion_inicial, orientacion)
    mostrar_matriz(nueva_matriz)
    return nueva_matriz

def sanar_mutaciones(matriz) -> List[List[str]]:
    """
    Sana las mutaciones presentes en la matriz de ADN.
    """
    sanador = Sanador("SanadorX", Detector(matriz))
    adn_sano = sanador.sanar_mutantes(matriz)
    print("\033[94m" + "El ADN sanado es:")
    mostrar_matriz(adn_sano)
    return adn_sano

def ingresar_nueva_matriz() -> List[List[str]]:
    """
    Solicita al usuario que ingrese una nueva matriz de ADN.

    Returns:
        List[List[str]]: Nueva matriz de ADN ingresada por el usuario.
    """
    nueva_matriz = []
    print("\033[94m " + "Ingrese las 6 filas de la matriz de ADN. Cada fila debe contener 6 bases nitrogenadas (A, T, C, G):")

    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").upper()
            if len(fila) == 6 and all(base in 'ATCG' for base in fila):
                nueva_matriz.append(list(fila))
                break
            else:
                print("\033[94m" + "Entrada inválida. Asegúrese de que la fila tenga 6 caracteres y solo contenga A, T, C, o G.")
    return nueva_matriz

def salir_menu() -> None:
    """
    Mensaje de salida del menú.
    """
    print("\033[94m" + "El ADN final es: ")
    mostrar_matriz(matriz)
    print("\033[94m" + "Saliendo del menú...")
    

def limpiar_terminal() -> None:
    """
    Limpia la terminal de comandos.
    """
    os.system('cls')

def mostrar_matriz(matriz_adn: List[List[str]]) -> None:
    """
    Muestra la matriz de ADN en un formato legible.

    Args:
        matriz_adn (List[List[str]]): Matriz de ADN a mostrar.
    """
    print("\033[94m" + "La matriz es la siguiente:")
    for fila in matriz_adn:
        print("\033[92m" + ' '.join(fila))

if __name__ == "__main__":
    main()
