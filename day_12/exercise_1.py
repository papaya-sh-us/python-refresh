import numpy as np

A = np.array([[4, 1],
              [2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)         
print(eigenvectors)

lam = eigenvalues[0]                
v = eigenvectors[:, 0]              
print(np.allclose(A @ v, lam * v))  