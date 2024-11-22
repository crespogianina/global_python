from clases import Detector, Virus, Radiacion, Sanador
import os

# matriz = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
matriz = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]

def main():
        menu()

def menu():
    while True:
        print("\033[1;36m"+"------------------MENÚ-------------------")
        print("\033[94m"+"|1. Detectar mutaciones")
        print("\033[94m"+"|2. Generar mutaciones")
        print("\033[94m"+"|3. Sanar ADN")
        print("\033[94m"+"|4. Salir del menu")
        print("\033[1;36m"+"-----------------------------------------")
        opcion = input("\033[97m" + "Ingrese una opcion: ")

        limpiar_terminal()

        if opcion == "1":
            detectar_mutaciones_matriz()
                
        elif opcion == "2":
            generar_mutaciones()
            
        elif opcion == "3":
            sanar_mutaciones()
            
        elif opcion == "4":
            salir_menu()
            break
        else:
            print("\033[94m"+"Debe ingresar una opcion valida.")
            print("\033[94m"+"Intente nuevamente.")



def detectar_mutaciones_matriz():
    print("\033[94m"+"Vamos a detectar mutaciones...")

    detector = Detector()
    mutacionesDetectadas = detector.detectar_mutantes(matriz)
    if mutacionesDetectadas:
        print("\033[94m"+"Se encontraron mutaciones en el ADN.")
        mostrar_matriz(matriz)
    else:
        print("\033[94m"+"No se encontraron mutaciones en el ADN.")

#GENERAR MUTACIONES
def generar_mutaciones():
    print("Generando mutaciones")
    print("\033[94m"+"Vamos a generar mutaciones")

    while True:

        print("\033[94m"+"¿Desea generar un virus o una radiacion?")
        mutacion =  input("\033[97m"+"Virus o Radiacion: ").lower()
        limpiar_terminal()

        if mutacion == "virus":
            print("Vamos a crear un virus")
            generar_virus()

            break
        elif mutacion == "radiacion":
            print("Vamos a crear una radiacion")
            generar_radiacion()
            break
        else: 
            print("Ingrese una opcion valida")

def generar_virus():

    print("\033[94m"+"Ingrese el nombre del virus: ") 
    nombre = input("\033[97m"+"Nombre: ").capitalize() 
    limpiar_terminal()
    
    if len(nombre) <= 0:
        print("Debe ingresar un nombre")
        generar_virus()
    else:

        print("\033[94m"+"Ingrese la posicion inicial (fila, columna):") 
        posicion_inicial = tuple(map(int, input("\033[97m"+"Posicion inicial: ").split(','))) 
        limpiar_terminal()

        nuevo_virus = agregar_base_nitrogenada(matriz, posicion_inicial, nombre)

        if nuevo_virus:
            mostrar_matriz(nuevo_virus)
        else:
            generar_virus()

def agregar_base_nitrogenada(matriz, posicion_inicial, nombre):
    
    print("\033[94m"+"Ingrese la base nitrogenada que desee") 
    print("\033[94m"+"| A | C | G | T |") 
    base = input("\033[97m"+"Ingrese la opcion: ").upper()
    
    limpiar_terminal()
    if(base in ["A", "C", "G", "T"]):
        
        virus = Virus(base, nombre, matriz)
        nuevo_virus = virus.crear_mutante(matriz, base, posicion_inicial)
        if nuevo_virus:
            print("Se creo correctamente el virus")
            
        else:
            print("Ocurrio un error")
        
        return nuevo_virus

    else:
        print("Ingrese una base nitrogenada valida")
        agregar_base_nitrogenada(matriz, posicion_inicial, nombre)
        

def generar_radiacion():
    while True:
        print("\033[94m"+"Ingrese el nombre de la radiacion: ") 
        nombre = input("\033[97m"+"Nombre: ").capitalize() 
        if len(nombre) <= 0:
            print("\033[94m"+"Debe ingresar un nombre para la raciacion")
        else:
            break
    
    while True:
        print("\033[94m"+"Ingrese la orientacion de la mutacion:") 
        print("\033[94m"+"Horizontal: H") 
        print("\033[94m"+"Vertical: V") 
        orientacion = input("\033[97m"+"Ingrese la opcion: ").upper()

        if orientacion != "H" and orientacion != "V":
            print("\033[94m"+"Debe ingresar una opcion valida") 
        else: 
            break
    
    print("\033[94m"+"Ingrese la posicion inicial (fila, columna):") 
    posicion_inicial = tuple(map(int, input("\033[97m"+"Posicion inicial: ").split(','))) 
    limpiar_terminal()

    while True:
        print("\033[94m"+"Ingrese la base nitrogenada que desee") 
        print("\033[94m"+"| A | C | G | T |") 
        base = input("\033[97m"+"Ingrese la opcion: ").upper()

        if(base in ["A", "C", "G", "T"]):

            print(nombre,base)
            radiacion = Radiacion(base, nombre, matriz)
            nueva_radiacion = radiacion.crear_mutante(radiacion, base, posicion_inicial, orientacion)
            print(nueva_radiacion)
            break
        else:
            print("Debe ingresar una opcion valida")
    


def sanar_mutaciones():
    print("\033[94m"+"Vamos a sanar el ADN.")
    adn_mutado = Sanador(matriz)
    
    
    while True:
        print("\033[94m"+"El AND es:")
        mostrar_matriz(matriz)
        print("\033[94m"+"Desea ingresar otro?")
        print("\033[94m"+"Si o No")
        nuevo = input("\033[97m"+"Ingrese la opcion: ").lower()
        if nuevo == 'no':
            adn_detector = Detector()
            adn_mutado = Sanador(adn_detector)

            adn_sano = adn_mutado.sanar_mutantes(matriz)
            print(adn_sano)
        elif nuevo == "si":
            print("\033[94m"+"Ingrese el nuevo ADN: ")
            nueva_matriz = ingresar_nueva_matriz()
            mostrar_matriz(nueva_matriz)
            break
        else:
            print("\033[94m"+"Ingrese una opcion valida: ")
        
def ingresar_nueva_matriz():
    nueva_matriz = []
    print("Ingrese las 6 filas de la matriz de ADN. Cada fila debe contener 6 bases nitrogenadas (A, T, C, G):")

    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").upper()
            if len(fila) == 6 and all(base in 'ATCG' for base in fila):
                nueva_matriz.append(fila)
                break
            else:
                print("Entrada inválida. Asegúrese de que la fila tenga 6 caracteres y solo contenga A, T, C, o G.")
    return nueva_matriz


def salir_menu():
    print("\033[94m"+"Saliendo del menu")

def limpiar_terminal():
    os.system('cls')

def mostrar_matriz(matriz):
    print("La matriz es la siguiente:")
    for fila in matriz:
        print(' '.join(fila))


    # mutante_vertical = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]
    # mutante_vertical = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]

main()