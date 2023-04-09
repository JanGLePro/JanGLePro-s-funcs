def resh(n):
    n += 1
    mas = [i % 2 for i in range(n)]
    mas[1] = 0
    mas[2] = 1
    prost = [2]

    for i in range(3, n):
        if mas[i]:
            prost.append(i)
            for k in range(i ** 2, n, i):
                mas[k] = 0

    return prost

# print(*resh(1000))
