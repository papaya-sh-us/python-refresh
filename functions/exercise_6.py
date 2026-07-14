def even_numbers():
    i = 1
    evens = []
    while i <= 20:
        if (i%2 == 0):
            evens.append(i)
        i += 1
    return evens
print(even_numbers())
