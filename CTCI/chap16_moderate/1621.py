def sum_swap(ns1, ns2):
    s1, s2 = sum(ns1), sum(ns2)
    diff = s1 - s2

    big, small = ns1, ns2
    if diff < 0:
        big, small = ns2, ns1

    if abs(diff) % 2 != 0: return None
    d = abs(diff) // 2

    smalls = set(small)
    for b in big:
        if b - d in smalls:
            return (b, (b - d))
    return None

print(sum_swap(
    [1,2,3], # 6
    [1,1,2] # 4
)) # (2, 1)
print(sum_swap(
    [4,1,2,1,1,2],
    [3,6,3,3]
)) # (3, 1)
