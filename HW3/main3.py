from matrix.matrix import Matrix
from matrix.mixinMatrix import MixinMatrix
import numpy as np

#3.1
np.random.seed(0)
matrix1_data = np.random.randint(0, 10, (10, 10))
matrix2_data = np.random.randint(0, 10, (10, 10))
matrix1 = Matrix(matrix1_data.tolist())
matrix2 = Matrix(matrix2_data.tolist())

result_add = matrix1 + matrix2
result_mul = matrix1 * matrix2
result_matmul = matrix1 @ matrix2

result_add.save_to_file("artifacts/3.1/matrixAdd.txt")
result_mul.save_to_file("artifacts/3.1/matrixMul.txt")
result_matmul.save_to_file("artifacts/3.1/matrixMatmul.txt")

#3.2
np.random.seed(0)
matrix1_data = np.random.randint(0, 10, (10, 10))
matrix2_data = np.random.randint(0, 10, (10, 10))
matrix1 = MixinMatrix(matrix1_data.tolist())
matrix2 = MixinMatrix(matrix2_data.tolist())

result_add = matrix1 + matrix2
result_mul = matrix1 * matrix2
result_matmul = matrix1 @ matrix2

result_add.save_to_file("artifacts/3.2/matrixAdd.txt")
result_mul.save_to_file("artifacts/3.2/matrixMul.txt")
result_matmul.save_to_file("artifacts/3.2/matrixMatmul.txt")

#3.3
np.random.seed(0)

A = None
C = None

while (True):
    A = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    B = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    C = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    D = B.copy()
    if hash(A) == hash(C) and not(A == C) and not (A @ B == C @ D):
        break

print(hash(A), hash(C))
A.save_to_file("artifacts/3.3/A.txt")
B.save_to_file("artifacts/3.3/B.txt")
C.save_to_file("artifacts/3.3/C.txt")
D.save_to_file("artifacts/3.3/D.txt")
(A @ B).save_to_file("artifacts/3.3/AB.txt")
(C @ D).save_to_file("artifacts/3.3/CD.txt")

with open("artifacts/3.3/hash.txt", 'w') as file:
    file.write(f"{hash(A @ B)} {hash(C @ D)}")