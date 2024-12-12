def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy.")

    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

    # obliczanie iloczynu macierzy
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

# przykładowe macierze
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(matrix_a, matrix_b)

print("Wynik mnożenia macierzy:")
for row in result:
    print(row)
