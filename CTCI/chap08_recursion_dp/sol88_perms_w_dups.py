from typing import Set

def perms_w_dups(s: str) -> Set[str]:
    if len(s) == 0:
        return set()
    if len(s) == 1:
        return set(s)
    curr, rest, results = s[0], s[1:], set()
    for p in perms_w_dups(rest):
        for i in range(len(p) + 1):
            result = p[:i] + curr + p[i:]
            if result in results:
                continue
            results.add(result)
            results.add(result)
    return results

print(perms_w_dups("")) # []
print(perms_w_dups("a")) # ["a"]
print(perms_w_dups("aa")) # ["aa"]
print(perms_w_dups("ab")) # ["ab", "ba"]
print(perms_w_dups("aba")) # ["aab", "aba", "baa"]
print(perms_w_dups("abba")) # ["aabb", "abab", "abba", "baab", "bbaa, "baba"]
