def powerset(xs, i=0, result=[[]]):
    if i == len(xs):
        return result
    curr = xs[i]
    with_curr = [r + [curr] for r in result]
    return powerset(xs, i+1, result + with_curr)

print(powerset([1,2,3]))
