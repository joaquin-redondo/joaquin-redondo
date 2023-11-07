# EJ N1 Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag para optimización: Si no hubo intercambios en esta pasada, la lista ya está ordenada
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambia los elementos si están en el orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # Si no hubo intercambios en esta pasada, la lista está ordenada
        if not swapped:
            break

# Ejemplo de uso
if __name__ == "__main__":
    try:
        input_str = input("Ingresa una lista de números separados por espacios: ")
        unsorted_list = [int(x) for x in input_str.split()]
        bubble_sort(unsorted_list)
        print("Lista ordenada:", unsorted_list)
    except ValueError:
        print("Por favor, ingresa una lista válida de números separados por espacios.")

# EJ N2 Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambia el elemento actual con el mínimo encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso
if __name__ == "__main__":
    try:
        input_str = input("Ingresa una lista de palabras separadas por espacios: ")
        unsorted_list = input_str.split()
        selection_sort(unsorted_list)
        print("Palabras ordenadas alfabéticamente:", " ".join(unsorted_list))
    except ValueError:
        print("Por favor, ingresa una lista válida de palabras separadas por espacios.")