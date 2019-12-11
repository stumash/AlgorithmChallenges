def strCompress(s):
    if len(s) < 1:
        return s
    ret = [s[0]]
    count = 1
    for c in s[1:]:
        if c == ret[-1]:
            count += 1
        else:
            ret.append(str(count))
            ret.append(c)
            count = 1
    ret.append(str(count))
    return "".join(ret) if len(ret) < len(s) else s

def test():
    srets = [
        ("aabcccccaaa", "a2b1c5a3")
    ]

    for s, ret in srets:
        print(strCompress(s) == ret)
