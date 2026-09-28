matriz = []

for i in range(2):
    fila = []
    for j in range(2):
        valor = input(f"ingrese  los datos para la posicion [{i}] [{j}]: ")
        fila.append(valor)
        matriz.append(fila)


print("la matriz ingresada de 2x2 es de: ")
for fila in matriz:
    print(fila)
