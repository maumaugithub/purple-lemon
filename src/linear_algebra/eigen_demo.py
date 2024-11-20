import numpy as np
A = np.array([[4, -2], [1,  1]])
print(A)
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)