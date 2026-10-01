import operaciones_matrices as op


def mostrar_menu():
    print("\n" + "=" * 60)
    print("      SISTEMA DE OPERACIONES CON MATRICES")
    print("=" * 40)
    print("1. Suma de dos matrices (3x3)")
    print("2. Multiplicación de dos matrices (2x2)")
    print("3. Generar Matriz Identidad (3x3)")
    print("4. Salir")
    print("=" * 40)


def main():
    manteners_activo = True

    while manteners_activo:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            op.sumar_matrices_3x3()
        elif opcion == "2":
            op.multiplicar_matrices_2x2()
        elif opcion == "3":
            op.generar_matriz_identidad()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            manteners_activo = False
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()