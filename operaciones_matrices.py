def leer_matriz(nombre, filas, columnas):
    print(f"\n--- Ingreso de datos para {nombre} ({filas}x{columnas}) ---")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


def sumar_matrices_3x3():
    matriz_a = leer_matriz("Matriz A", 3, 3)
    matriz_b = leer_matriz("Matriz B", 3, 3)

    matriz_suma = []
    for i in range(3):
        fila_suma = []
        for j in range(3):
            suma_posicion = matriz_a[i][j] + matriz_b[i][j]
            fila_suma.append(suma_posicion)
        matriz_suma.append(fila_suma)

    print("\n--- Matriz Resultante (A + B) ---")
    mostrar_matriz(matriz_suma)


def multiplicar_matrices_2x2():
    matriz_a = leer_matriz("Matriz A", 2, 2)
    matriz_b = leer_matriz("Matriz B", 2, 2)

    matriz_c = []
    for i in range(2):
        fila = []
        for j in range(2):
            suma = 0
            for k in range(2):
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila.append(suma)
        matriz_c.append(fila)

    print("\n--- Matriz Resultante (A x B) ---")
    mostrar_matriz(matriz_c)


def generar_matriz_identidad():
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\n--- Matriz Base Inicial ---")
    mostrar_matriz(matriz1)

    largo = len(matriz1)
    for i in range(largo):
        for j in range(largo):
            if i == j:
                matriz1[i][j] = 1
            else:
                matriz1[i][j] = 0

    print("\n--- Matriz Identidad Resultante ---")
    mostrar_matriz(matriz1)