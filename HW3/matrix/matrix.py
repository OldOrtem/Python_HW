import numpy as np

class HashMixin:
    # полиномиальная хеш функция каждый элемент умножается на число и складывается в сумму по простому модулю
    def __hash__(self):
        k = 2 ** 10 - 1
        mod = 2 ** 10 - 3
        sum = 0
        for row in self.data:
            for item in row:
                sum = (sum + (item * k)%mod)%mod
        return sum

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data

class Matrix(HashMixin):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape for addition.")
        return Matrix(
            [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape for element-wise multiplication.")
        return Matrix(
            [[self.data[i][j] * other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Matrix dimensions do not align for matrix multiplication.")
        result = np.zeros((self.shape[0], other.shape[1]), dtype=int)
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(self.shape[1]):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result.tolist())

    @property
    def shape(self):
        return (len(self.data), len(self.data[0]))

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        return str(self.data)

    def copy(self):
        new_data = [row[:] for row in self.data]
        return Matrix(new_data)
