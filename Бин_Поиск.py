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
