# 3d matrix operations
import numpy as np
class Matrix:
    def __init__(self, m):
        self.m = m

    def __add__(self, other):
        return np.add(self.m, other.m)

    def __sub__(self, other):
        return np.subtract(self.m, other.m)

    def __mul__(self, other):
        return np.dot(self.m, other.m)

    def __str__(self):
        return str(self.m)

    def determinant(self):
        return np.linalg.det(self.m)

    def transpose(self):
        return np.transpose(self.m)


matrix = Matrix([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
matrix2 = Matrix([[5, 6, 1], [7, 8, 9], [9, 10, 11]])
print('\nMatriks 1 : ',matrix)
print('Matriks 2 : ',matrix2)
print('\nMatriks 1 + Matriks 2 : \n',matrix+matrix2)
print('\nMatriks 1 - Matriks 2 : \n',matrix-matrix2)
print('\nMatriks 1 * Matriks 2 : \n',matrix*matrix2)
print('\nDeterminan Matriks 1 : ',matrix.determinant())
print('\nTranspose Matriks 1 : \n',matrix.transpose())

