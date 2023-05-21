def searchMatrix(matrix, target: int) -> bool:
    L, R = 0, len(matrix) - 1
    while R >= L:
        M = (R + L) // 2
        row = matrix[M]
        L2, R2 = 0, len(row) - 1
        while R2 >= L2:
            M2 = (R2 + L2) // 2

            if row[M2] == target:
                return True
            # Check Right side
            elif target > row[M2]:
                L2 = M2 + 1
                L = M + 1
            # Check Left side
            else:
                R2 = M2 - 1
                R = M - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(searchMatrix(matrix, target))
