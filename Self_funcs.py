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


def bit_masks(mas):
    n = len(mas)
    all_masks = []
    for mask in range(1 << n):
        this_mask = []
        for i in range(n):
            if mask & (1 << i):
                this_mask.append(mas[i])
        all_masks.append(this_mask)
    return all_masks

    # for item in bit_masks([1, 2, 3, 4]):
    #     print(item)


def bin_search(mas, n):
    l = 0
    r = len(mas)
    while r - l > 1:
        mid = l + (r - l) // 2
        if mas[mid] < n:
            l = mid
        elif mas[mid] > n:
            r = mid
        else:
            print(f'ind={mid}')
            return None
    print(f'between {l} and {r} indexes')

    # list1 = [12, 24, 32, 39, 45, 50, 54]
    # n = 40
    # bin_search(list1, n)
