matriz = [
    [1, 2],
    [3, 4]
]

for fila in matriz:
    print(fila)

#Escalar
k = 5

matriz2 = []

for i in range(len(matriz)):
    matriz2.append([])
    for j in range(len(matriz)):
        matriz2[i].append(k * matriz[i][j])

print("="*13)
print("Escalar ", k)
for fila in matriz2:
    print(fila)