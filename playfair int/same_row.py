# check if the Pair letter, in the same row or not,
# if in the same row, replace the letter by the next letter
# but if the letter in the last position in the array, it should be replaced by the first letter in the array.

def samerow(charA, charB):
    matrix = [['E', 'X', 'A', 'M', 'P'],
              ['L', 'B', 'C', 'D', 'F'],
              ['G', 'H', 'I', 'K', 'N'],
              ['O', 'Q', 'R', 'S', 'T'],
              ['U', 'V', 'W', 'Y', 'Z']]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == charA):
                a = [i, j]
            if (matrix[i][j] == charB):
                b = [i, j]
    print(a[1], b[1])
    if (a[0] == b[0]):
        if (a[1] == 4):
            matrix[a[0]][a[1]] = matrix[a[0]][0]
            matrix[b[0]][b[1]] = matrix[b[0]][b[1]+1]
        elif (b[1] == 4):
            matrix[b[0]][b[1]] = matrix[b[0]][0]
            matrix[a[0]][a[1]] = matrix[a[0]][a[1]+1]
        else:
            matrix[a[0]][a[1]] = matrix[a[0]][a[1]+1]
            matrix[b[0]][b[1]] = matrix[b[0]][b[1]+1]

    return matrix


print(samerow('G', 'N'))
