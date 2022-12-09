with open("Day 8/input.in", "r") as f:
    data = f.readlines()

matrix = [[int(x) for x in line.strip()] for line in data]
max_scenic = 0

for i in range(0, len(matrix)): # row
    for j in range(0, len(matrix[i])):

        tree_house = matrix[i][j]

        trees_left = 0
        if j != 0:
            left = list(reversed([matrix[i][k] for k in range(j)]))
            for tree in left:
                if tree >= tree_house:
                    trees_left += 1
                    break
                trees_left += 1

        trees_right = 0
        if j != len(matrix[i]) - 1:
            right = [matrix[i][k] for k in range(j + 1, len(matrix[i]))]
            for tree in right:
                if tree >= tree_house:
                    trees_right += 1
                    break
                trees_right += 1

        trees_top = 0
        if i != 0:
            top = list(reversed([matrix[k][j] for k in range(i)]))
            for tree in top:
                if tree >= tree_house:
                    trees_top += 1
                    break
                trees_top += 1

        trees_bottom = 0
        if i != len(matrix) - 1:
            bottom = [matrix[k][j] for k in range(i + 1, len(matrix))]
            for tree in bottom:
                if tree >= tree_house:
                    trees_bottom += 1
                    break
                trees_bottom += 1

        scenic = trees_left * trees_right * trees_top * trees_bottom
        max_scenic = scenic if scenic > max_scenic else max_scenic

print(max_scenic)