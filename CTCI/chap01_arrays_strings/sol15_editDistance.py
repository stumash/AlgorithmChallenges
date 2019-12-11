from functools import partial

def withinEdit(n, s1, s2):
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            break
    else:
        i += 1

    # crazy way to do a base case in recursion
    f = partial(withinEdit, n-1) if n > 1 else (lambda a,b: a == b)

    return any([
        f(s1[i+1:], s2[i:]),
        f(s1[i:]  , s2[i+1:]),
        f(s1[i+1:], s2[i+1:])
    ])

def withinOneEdit(s1, s2):
    return withinEdit(1, s1, s2)

def withinTwoEdit(s1, s2):
    return withinEdit(2, s1, s2)

def test_withinOneEdit():
    ssb = [
        (("pale", "ple"), True),
        (("pales", "pale"), True),
        (("pale", "bale"), True),
        (("pale", "bake"), False)
    ]

    for (s1, s2), b in ssb:
        print(withinOneEdit(s1, s2)==b)

def test_withinTwoEdit():
    ssb = [
        (("pale", "bake"), True),
        (("pales", "bake"), False),
    ]

    for (s1, s2), b in ssb:
        print(withinTwoEdit(s1, s2)==b)
