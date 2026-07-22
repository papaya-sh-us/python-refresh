v1 = [1,2,3]
v2 = [4,5,6]

def dot(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

print(dot(v1,v2))

import numpy as np
def numpy_dot(a,b):
    print(np.dot(a, b))         
    print(a @ b)                
    print(np.sum(a * b))        

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

numpy_dot(a,b)
