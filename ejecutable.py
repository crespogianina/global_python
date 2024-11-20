from clases import Detector

def main():
        matriz = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    # mutante_horizontal = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    # mutante_vertical = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]7
    # mutante_vertical = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]
        detector = Detector()

        detector.detectar_mutantes(matriz)

        print("ADN Inicial: ")
        for fila in matriz:
            print(fila)
            menu()

def menu():
    print("Menu: ")
    print("1. Detectar mutaciones")
    print("2. Generar mutaciones")
    print("3. Sanar ADN")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("Vamos a detectar mutaciones.")
    elif opcion == "2":
        print("Vamos a generar mutaciones.")
    elif opcion == "3":
        print("Vamos a sanar el ADN.")
    else:
        print("Debe ingresar una opcion valida.")
        print("Intente nuevamente.")


main()