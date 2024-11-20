from clases import Detector, Virus, Radiacion
import os

# matriz = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
matriz = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]

def limpiar_terminal():
    os.system('cls')
    

def main():
        menu()

def menu():
    while True:
        print("\033[94m"+"------------------MENÚ-------------------")
        print("\033[94m"+"|1. Detectar mutaciones")
        print("\033[94m"+"|2. Generar mutaciones")
        print("\033[94m"+"|3. Sanar ADN")
        print("\033[94m"+"|4. Salir del menu")
        print("\033[94m"+"-----------------------------------------")
        opcion = input("\033[97m" + "Ingrese una opcion: ")

        limpiar_terminal()
        if opcion == "1":
            print("\033[94m"+"Vamos a detectar mutaciones...")

            detector = Detector()
            mutacionesDetectadas = detector.detectar_mutantes(matriz)

            if mutacionesDetectadas:
                print("\033[94m"+"Se encontraron mutaciones.")
            else:
                print("\033[94m"+"No se encontraron mutaciones.")
                
        elif opcion == "2":
            while True:
                print("\033[94m"+"Vamos a generar mutaciones....")
                print("\033[94m"+"¿Desea generar un virus o una radiacion?")
                opcion = input("\033[97m"+"Virus o Radiacion: ").lower()
                print(opcion)

                if opcion == "virus":
                    while True:
                        print("\033[94m"+"Ingrese la base nitrogenada que desee")
                        print("\033[94m"+"| A | C | G | T |")
                        base = input("Ingrese la opcion: ").upper()
                        if base == "A" or base == "C" or base == "G" or base == "T":
                        # virus = Virus()
                            print("\033[94m"+"Creando virus....")
                            break
                        else:
                            print("Ingrese una opcion valida")

                elif opcion == "radiacion":
                    radiacion = Radiacion()
                    print("Creando radiacion....")
                    break
                else:
                    print("Ingrese una opcion valida")

            
        elif opcion == "3":
            print("Vamos a sanar el ADN.")
        elif opcion == "4":
            print("Saliendo del menu....")
            break
        else:
            print("Debe ingresar una opcion valida.")
            print("Intente nuevamente.")


main()


    # mutante_vertical = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]
    # mutante_vertical = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]