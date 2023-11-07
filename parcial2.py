# defino para hacer la verificaion de las letras
def enter_letters():
    dna = []

    for i in range(6):
#hago un for para empezar a pedir las letras
        fila = input("Ingrese la fila de ADN (6 letras): ").strip()
#pido que ingrese las letras
        if len(fila) != 6 or not all(c in "ATCG" for c in fila):
            print("Entrada no válida. Debe contener exactamente 6 letras de 'A', 'T', 'C' o 'G'.")
#verifico que sean 6 letras y las correspondientes
            return
#si esta mal lo devuelvo
        dna.append(fila)
#el .append es para que me lo vaya enlistando
    return dna


#funcion de entrada:
def is_mutant(dna):
    
    # número de filas 
    rows = len(dna)
    # número de columnas 
    cols = len(dna)
    
    # función para empezar a verificar
    def structure(f, c):
        return 0 <= f < rows and 0 <= c < cols
        
    # verifico la vertical
    def vertical(f, c):
        for i in range(4):
            if not (structure(f+i, c) and dna[f][c] == dna[f+i][c]):
                return False
        return True
    
    
    # verifico horizontal
    def horizontal(f, c):
        for i in range(4):
            if not (structure(f, c+i) and dna[f][c] == dna[f][c+i]):
                return False
        return True
    
    # verificamos la diagonal
    def diagonal(f, c):
        for i in range(4):
            if not (structure(f+i, c+i) and dna[f][c] == dna[f+i][c+i]):
                return False
        return True
    
    #empezamos a iterar
    for f in range(rows):
        for c in range(cols):
            # Verificamos si hay mutante de forma horizontal, vertical o diagonal 
            if ( vertical(f, c) or horizontal(f,c) or diagonal(f, c)):
                return True
    
    # Si no hay mutantes , lo devuelvo en forma false
    return False

dna=enter_letters()
#le doy el valor a dna
     
if is_mutant(dna) :
    print("El ADN es mutante.")
#chqueo final
else:
    print("No es mutante")



#CASOS DE PRUEBA
'''
dna = [
    'ATGCGA',
    'CAGTGC',
    'TTATGT',
    'AGAAGG',
    'CCCCTA',
    'TCACTG'
]
'''
# Debería detectar una secuencia mutante.

#CASO 2
'''
dna = [
    'ATGCGA',
    'CAGTGC',
    'TTATTT',
    'AGAAGG',
    'CCCTAG',
    'TCACTA'
]
'''
# Debería detectar mutante.

#CASO 3
'''
dna = [
    'ATGCGA',
    'CAGTGC',
    'TAGTTT',
    'AGAAGG',
    'GCCCTA',
    'TCACTA'
]
'''
# No debería detectar mutante.
