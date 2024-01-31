import numpy as np

class Matrix(np.ndarray):
    def __new__(cls, array):
        return np.asarray(array).view(cls)

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = Matrix(data)
print(matrix)