import numpy as np

def sort_eigenpairs(eigenvalues, eigenvectors):
    order = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[order]
    sorted_eigenvectors = eigenvectors[:, order]
    return sorted_eigenvalues, sorted_eigenvectors


A = np.array([[2, 1],
              [1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Original eigenvalues:", eigenvalues)

sorted_vals, sorted_vecs = sort_eigenpairs(eigenvalues, eigenvectors)
print("Sorted eigenvalues:", sorted_vals)
print("Sorted eigenvectors:\n", sorted_vecs)

for i in range(len(sorted_vals)):
    v = sorted_vecs[:, i]
    lam = sorted_vals[i]
    left_side = A @ v
    right_side = lam * v
    print(f"\nPair {i}: eigenvalue = {lam}")
    print("A @ v      =", left_side)
    print("lambda * v =", right_side)
    print("Match?", np.allclose(left_side, right_side))