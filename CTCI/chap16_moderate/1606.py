def binary_search_smaller(n, ns):
    left, right = 0, len(ns)-1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        curr = ns[mid]
        if n == curr:
            return curr
        elif curr < n:
            left = mid + 1
        elif curr > n:
            right = mid - 1
    if ns[mid] < n:
        return ns[mid]
    elif ns[mid] > n:
        if ns[mid - 1] < n:
            return ns[mid - 1]
    return None

def smallest_difference(ns1, ns2):
    min_diff = None
    ns2.sort()
    for n in ns1:
        found = binary_search_smaller(n, ns2)
        if found and (min_diff is None or min_diff > n - found):
            min_diff = n - found
    return min_diff

print(smallest_difference([1, 3, 18, 11, 2], [23, 127, 235, 19, 8])) # 3
