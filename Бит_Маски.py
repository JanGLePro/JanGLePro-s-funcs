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
