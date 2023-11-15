def is_mutant(dna):
    cont = 0

    for i in range(len(dna)):
        for j in range(len(dna[0])):
            # Verificar filas
            if j + 3 < len(dna[0]) and dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                cont += 1
                if cont > 1:
                    return True

            # Verificar columnas
            if i + 3 < len(dna) and dna[i][j] == dna[i + 1][j] == dna[i + 2][j] == dna[i + 3][j]:
                cont += 1
                if cont > 1:
                    return True

            # Verificar diagonales descendentes
            if i + 3 < len(dna) and j + 3 < len(dna[0]) and dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                cont += 1
                if cont > 1:
                    return True

            # Verificar diagonales ascendentes
            if i - 3 >= 0 and j + 3 < len(dna[0]) and dna[i][j] == dna[i - 1][j + 1] == dna[i - 2][j + 2] == dna[i - 3][j + 3]:
                cont += 1
                if cont > 1:
                    return True

    return False





def ingresar_fila():
    while True:
        fila = input("Ingrese una fila (solo letras A, T, C, G): \n").upper().replace(" ", "")

        # Verificar que la fila tenga exactamente 6 caracteres
        if len(fila) == 6:
            # Verificar que solo se ingresen letras permitidas
            if all(letra in 'ATCG' for letra in fila):
                return list(fila)
            else:
                print("Por favor, ingrese solo las letras válidas 'A', 'T', 'C', 'G'")
        else:
            print("La fila debe tener exactamente 6 caracteres")

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

dna = [[' ']*6 for _ in range(6)]

for i in range(6):
    dna[i] = ingresar_fila()

print("\nMatriz Resultante:")
mostrar_matriz(dna)

print("\n Resultado de la prueba de mutación: \n --------------- \n", "Es mutante" if is_mutant(dna) else "No es mutante", "\n --------------- " )
