import numpy as np

A = np.array([[3, 1],
              [2, 4]])
print(np.linalg.det(A))    

#det > 0 — the transformation preserves orientation, scaling area by that factor.
#det = 0 — the matrix squashes space into a lower dimension. Information is destroyed; it cannot be undone. The matrix is called singular.
#det < 0 — orientation is flipped (mirrored), area scaled by |det|.

A_inv = np.linalg.inv(A)
print(A @ A_inv)