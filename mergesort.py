def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]

    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)

    print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")
    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Comparar elementos de ambas listas y agregarlos en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes (si hay)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

# Ejemplo de uso:
lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

