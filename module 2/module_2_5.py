def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrix(3, 2, 77)
result2 = get_matrix(2, 7, 'XX')
result3 = get_matrix(4, 4, [5, 8])
print(result1)
print(result2)
print(result3)