v1 = [1,2,3]
v2 = [4,5,6]

def dot(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

print(dot(v1,v2))
