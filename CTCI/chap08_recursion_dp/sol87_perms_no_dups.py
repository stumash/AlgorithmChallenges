from typing import List

def perms_no_dups(s: str) -> List[str]:
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]

    c = s[0]
    result = []
    for p in perms_no_dups(s[1:]):
        for i in range(len(p) + 1):
            result.append(p[:i] + c + p[i:])
    return result

print(perms_no_dups("")) # []
print(perms_no_dups("a")) # ['a']
print(perms_no_dups("ab")) # ['ab', 'ba']
print(perms_no_dups("abc")) # ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
