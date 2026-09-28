
def leer_matriz(nombre):
    print(f"\n--- Ingreso de datos para la {nombre} (3x3) ---")
    matriz = []
    for i in range(3):
        fila = []
        for j in range(3):
            valor = float(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


matriz_a = leer_matriz("Matriz A")
matriz_b = leer_matriz("Matriz B")


matriz_suma = []
for i in range(3):
    fila_suma = []
    for j in range(3):
        suma_posicion = matriz_a[i][j] + matriz_b[i][j]
        fila_suma.append(suma_posicion)
    matriz_suma.append(fila_suma)


print("\n--- Matriz Resultante (A + B) ---")
mostrar_matriz(matriz_suma)