import numpy as np

def matmul_loop(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("shapes do not match: " + str((rows_A, cols_A)) + " and " + str((rows_B, cols_B)))

    result = []
    for i in range(rows_A):
        new_row = []
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total = total + A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


A1 = [[1, 2],
      [3, 4]]

B1 = [[5, 6],
      [7, 8]]

result1 = matmul_loop(A1, B1)
print("result1:", result1)

check1 = np.allclose(np.array(result1), np.array(A1) @ np.array(B1))
print("matches numpy:", check1)


A2 = [[1, 2, 3],
      [4, 5, 6]]

B2 = [[7, 8],
      [9, 10],
      [11, 12]]

result2 = matmul_loop(A2, B2)
print("result2:", result2)

check2 = np.allclose(np.array(result2), np.array(A2) @ np.array(B2))
print("matches numpy:", check2)


A3 = [[1, 2, 3],
      [4, 5, 6]]

B3 = [[1, 2, 3],
      [4, 5, 6]]

try:
    result3 = matmul_loop(A3, B3)
    print("result3:", result3)
except ValueError as e:
    print("got error:", e)