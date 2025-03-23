def spiralOrder(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = [list(x) for x in zip(*matrix)][::-1]
    return res

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))
