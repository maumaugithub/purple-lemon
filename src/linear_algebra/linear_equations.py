import numpy as np
A = np.array([[3, 2], [1, 1]])  # Coefficient matrix
b = np.array([5, 4])  # Right-hand side
print(A)
print(b)
x = np.linalg.solve(A, b)  # Solution vector
print(x)
det = np.linalg.det(A)
print(det)