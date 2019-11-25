# merge sort, not in place. returns sorted copy

def mergesorted(items):
    if not len(items) > 1:
        return items

    mid = len(items) // 2

    lo_half = mergesorted(items[:mid])
    hi_half = mergesorted(items[mid:])

    # i had
    # lo_half = mergesorted(items[:mid])
    # hi_half = mergesorted(items[:mid])

    return _merged(lo_half, hi_half)

def _merged(items1, items2):
    merged = list()

    i, j = 0, 0
    k = 0
    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            merged.append( items1[i] )
            i += 1
        else:
            merged.append( items2[j] )
            j += 1

    while i < len(items1):
        merged.append( items1[i] )
        i += 1
    while j < len(items2):
        merged.append( items2[j] )
        j += 1

    return merged
