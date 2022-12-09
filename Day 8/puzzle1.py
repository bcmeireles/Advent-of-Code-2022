with open("Day 8/input.in", "r") as f:
    data = f.readlines()

matrix = [[int(x) for x in line.strip()] for line in data]
visible = []

matrix.insert(0, [0 for _ in range(len(matrix[0]))])
matrix.append([0 for _ in range(len(matrix[0]))])
for row in matrix:
    row.insert(0, 0)
    row.append(0)

for i in range(1, len(matrix) - 1): # row
    for j in range(1, len(matrix[i]) - 1):
        if i == 1 or j == 1 or i == len(matrix) - 2 or j == len(matrix[i]) - 2:
            if (i, j) not in visible:
                visible.append((i, j))

        # check if tree is visible from the left
        # check if matrix[i][j] is bigger than all numbers in the columns to the left and in the same row
        if all(matrix[i][j] > tree for tree in [matrix[i][k] for k in range(j)]):
            if (i, j) not in visible:
                visible.append((i, j))

        # check if tree is visible from the right
        # check if matrix[i][j] is bigger than all numbers in the columns to the right and in the same row
        if all(matrix[i][j] > tree for tree in [matrix[i][k] for k in range(j + 1, len(matrix[i]))]):
            if (i, j) not in visible:
                visible.append((i, j))

        # check if tree is visible from the top
        # check if matrix[i][j] is bigger than all numbers in the rows above and in the same column
        if all(matrix[i][j] > tree for tree in [matrix[k][j] for k in range(i)]):
            if (i, j) not in visible:
                visible.append((i, j))

        # check if tree is visible from the bottom
        # check if matrix[i][j] is bigger than all numbers in the rows below and in the same column
        if all(matrix[i][j] > tree for tree in [matrix[k][j] for k in range(i + 1, len(matrix))]):
            if (i, j) not in visible:
                visible.append((i, j))

print(len(visible))       