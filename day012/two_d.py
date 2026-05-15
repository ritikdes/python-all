matrix = [[1,2,3,],
              [4,5,6,],
              [7,8,9]]

for row in matrix:
    print(row)


diagonal_sum = matrix[0][0] + matrix[1][1] + matrix[2][2]
print(diagonal_sum)

diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)

new_matrix = [[0,0,0] for _ in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        new_matrix[i][j] = matrix[j][i]
print(new_matrix)