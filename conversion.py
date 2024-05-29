# conversion.py

def kg_to_libras(kg):
    return kg * 2.20462

def libras_to_kg(libras):
    return libras / 2.20462

def kg_to_gramos(kg):
    return kg * 1000

def kg_to_miligramos(kg):
    return kg * 1000000

def main():
    while True:
        print("Aplicación de Conversión de Peso")
        print("1. Kilogramos a Libras")
        print("2. Libras a Kilogramos")
        print("3. Kilogramos a Gramos")
        print("4. Kilogramos a Miligramos")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        valor = float(input("Ingrese el valor a convertir: "))

        if opcion == "1":
            print("Resultado:", kg_to_libras(valor), "libras")
        elif opcion == "2":
            print("Resultado:", libras_to_kg(valor), "kilogramos")
        elif opcion == "3":
            print("Resultado:", kg_to_gramos(valor), "gramos")
        elif opcion == "4":
            print("Resultado:", kg_to_miligramos(valor), "miligramos")
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()