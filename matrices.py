matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
num_filas = len(matriz)
num_columnas = len(matriz)
for i in range(num_filas):
    for j in range(num_columnas):
        elemento = matriz[i][j]
        print(f"Elemento en ({i}, {j}) es {elemento}")
for fila_actual in matriz:
    for elemento in fila_actual:
        print(elemento, end=" ")
    print()