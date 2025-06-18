def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Prueba con impresión
lista_a_ordenar = [54, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_a_ordenar}") 
ordenamiento_burbuja(lista_a_ordenar)
print(f"Lista ordenada: {lista_a_ordenar}")

# Casos de prueba

# caso 1: lista desordenada
lista1 = [6, 3, 8, 2, 5]
ordenamiento_burbuja(lista1)
assert lista1 == [2, 3, 5, 6, 8]

# caso 2: lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
ordenamiento_burbuja(lista2)
assert lista2 == [1, 2, 3, 4, 5]

# caso 3: lista ordenada a la inversa (peor caso)
lista3 = [5, 4, 3, 2, 1]
ordenamiento_burbuja(lista3)
assert lista3 == [1, 2, 3, 4, 5]

# caso 4: lista con elementos duplicados
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_burbuja(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8]

# casos borde
assert ordenamiento_burbuja([]) == []
assert ordenamiento_burbuja([42]) == [42]
print("¡Todas las pruebas pasaron!")