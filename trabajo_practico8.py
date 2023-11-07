#ejercicio 1
def contar_digitos(n):
    if n < 0:
        raise ValueError("El número debe ser positivo.")
    if n == 0:
        return 1  # El número 0 tiene un dígito.
    count = 0
    while n > 0:
        count += 1
        n //= 10  # Eliminar el último dígito.
    return count

#ejercicio 2
def es_potencia_de(n, b):
    if n <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser positivos.")
    if n == 1:
        return True  # Cualquier número es una potencia de 1.
    power = 1
    while power < n:
        power *= b
    return power == n

#ejercicio 3
def encontrar_posiciones(subcadena, cadena, inicio=0, resultados=None):
    if resultados is None:
        resultados = []

    posicion = cadena.find(subcadena, inicio)
    if posicion != -1:
        resultados.append(posicion)
        encontrar_posiciones(subcadena, cadena, posicion + 1, resultados)

    return resultados

#ejercicio 4
def par(n):
    if n == 0:
        return True
    return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    return par(n - 1)

#ejercicio 5
def encontrar_mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        sub_max = encontrar_mayor(lista[1:])
        return lista[0] if lista[0] > sub_max else sub_max


#ejercicio 6
def replicar(lista, n):
    if n == 0:
        return []
    return lista + replicar(lista, n - 1)
